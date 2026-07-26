// Inserts the chat widget <script> tag before </body> on every site HTML page.
// Run: node chatbot/inject-widget.js

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const EXCLUDE_DIRS = new Set([
  "node_modules", ".git", ".claude", ".github", "_archive", "docs", "chatbot",
]);
const TAG = '<script src="/shared/chat-widget.js" defer></script>';

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

let changed = 0;
let skipped = 0;
for (const file of findHtmlFiles(ROOT)) {
  const html = fs.readFileSync(file, "utf8");
  if (html.includes("chat-widget.js")) {
    skipped++;
    continue;
  }
  if (!html.includes("</body>")) {
    console.log(`  no </body>, skipping: ${file}`);
    continue;
  }
  const updated = html.replace("</body>", `  ${TAG}\n</body>`);
  fs.writeFileSync(file, updated);
  changed++;
}

console.log(`Injected widget into ${changed} files (${skipped} already had it).`);
