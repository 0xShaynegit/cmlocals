// Extracts <main> text from every site page and splits it into embeddable chunks.
// Run: node chatbot/build-chunks.js
// Output: chatbot/content-chunks.json

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const ROOT = path.resolve(__dirname, "..");
const EXCLUDE_DIRS = new Set([
  "node_modules", ".git", ".claude", ".github", "_archive", "docs",
  "css", "js", "fonts", "images", "shared", "scripts", "chatbot", "tools",
]);
const CHUNK_SIZE = 900;   // chars
const CHUNK_OVERLAP = 150;

function findHtmlFiles(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith(".")) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (EXCLUDE_DIRS.has(entry.name)) continue;
      findHtmlFiles(full, out);
    } else if (entry.isFile() && entry.name.endsWith(".html")) {
      out.push(full);
    }
  }
  return out;
}

function decodeEntities(str) {
  return str
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#0?39;/g, "'")
    .replace(/&nbsp;/g, " ")
    .replace(/&mdash;/g, "-")
    .replace(/&ndash;/g, "-")
    .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)));
}

function htmlToText(html) {
  return decodeEntities(
    html
      .replace(/<!--[\s\S]*?-->/g, " ")
      .replace(/<(script|style|nav|svg|noscript)[\s\S]*?<\/\1>/gi, " ")
      .replace(/<\/(p|div|section|li|h[1-6]|br|tr)>/gi, "\n")
      .replace(/<[^>]+>/g, " ")
  )
    .replace(/[ \t]+/g, " ")
    .replace(/\n\s*\n+/g, "\n")
    .split("\n")
    .map((l) => l.trim())
    .filter(Boolean)
    .join("\n");
}

function urlFor(filePath) {
  let rel = path.relative(ROOT, filePath).replace(/\\/g, "/");
  if (rel === "index.html") return "/";
  if (rel.endsWith("/index.html")) return "/" + rel.slice(0, -"index.html".length);
  return "/" + rel;
}

function chunkText(text, title, url) {
  const chunks = [];
  let start = 0;
  while (start < text.length) {
    const end = Math.min(start + CHUNK_SIZE, text.length);
    let slice = text.slice(start, end);
    if (end < text.length) {
      const lastBreak = Math.max(slice.lastIndexOf("\n"), slice.lastIndexOf(". "));
      if (lastBreak > CHUNK_SIZE * 0.5) slice = slice.slice(0, lastBreak + 1);
    }
    const body = slice.trim();
    if (body.length > 40) {
      chunks.push({ url, title, text: body });
    }
    const advance = Math.max(slice.length - CHUNK_OVERLAP, Math.floor(CHUNK_SIZE * 0.25));
    start += advance;
    if (end >= text.length) break;
  }
  return chunks;
}

function main() {
  const files = findHtmlFiles(ROOT);
  const allChunks = [];

  for (const file of files) {
    const html = fs.readFileSync(file, "utf8");
    const titleMatch = html.match(/<title>([\s\S]*?)<\/title>/i);
    const title = titleMatch ? decodeEntities(titleMatch[1].trim()) : path.basename(file);
    const mainMatch = html.match(/<main[^>]*>([\s\S]*?)<\/main>/i);
    if (!mainMatch) continue;

    const text = htmlToText(mainMatch[1]);
    if (text.length < 80) continue;

    const url = urlFor(file);
    const chunks = chunkText(text, title, url);
    // Vectorize IDs are capped at 64 bytes; hash the URL so long slugs never
    // overflow that (the real url still lives in metadata for display/links).
    const urlHash = crypto.createHash("sha1").update(url).digest("hex").slice(0, 16);
    chunks.forEach((c, i) => {
      allChunks.push({ id: `${urlHash}#${i}`, ...c });
    });
  }

  const outPath = path.join(__dirname, "content-chunks.json");
  fs.writeFileSync(outPath, JSON.stringify(allChunks, null, 2));
  console.log(`Extracted ${allChunks.length} chunks from ${files.length} html files -> ${outPath}`);
}

main();
