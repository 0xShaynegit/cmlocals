// Deletes vectors from the index whose IDs no longer exist in content-chunks.json
// (e.g. a page or section was removed). Run after upsert.
// Usage: node chatbot/prune-stale-vectors.js [--index=cmlocals-content]

const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");

// Chunk IDs are our own generated `/url/#index` slugs (letters, digits, /, -, #
// only), never external input, so shell:true here carries no injection risk.
const IS_WINDOWS = process.platform === "win32";

const args = Object.fromEntries(
  process.argv.slice(2).map((a) => {
    const [k, v] = a.replace(/^--/, "").split("=");
    return [k, v ?? true];
  })
);
const INDEX_NAME = args.index || "cmlocals-content";

const chunks = JSON.parse(fs.readFileSync(path.join(__dirname, "content-chunks.json"), "utf8"));
const currentIds = new Set(chunks.map((c) => c.id));

function listAllVectorIds() {
  const ids = [];
  let cursor;
  for (;;) {
    const cmdArgs = ["wrangler", "vectorize", "list-vectors", INDEX_NAME, "--count", "200", "--json"];
    if (cursor) cmdArgs.push(`--cursor=${cursor}`);
    const out = execFileSync("npx", cmdArgs, {
      encoding: "utf8",
      maxBuffer: 1024 * 1024 * 50,
      shell: IS_WINDOWS,
    });
    const json = JSON.parse(out);
    (json.vectors || []).forEach((v) => ids.push(v.id));
    if (!json.nextCursor || json.vectors.length === 0) break;
    cursor = json.nextCursor;
  }
  return ids;
}

function main() {
  const existingIds = listAllVectorIds();
  const staleIds = existingIds.filter((id) => !currentIds.has(id));

  if (staleIds.length === 0) {
    console.log("No stale vectors to prune.");
    return;
  }

  console.log(`Pruning ${staleIds.length} stale vectors...`);
  // Kept small: Windows has an ~8KB command-line length limit, and each id
  // (a short hash + #index) still adds up fast across hundreds of vectors.
  const BATCH = 100;
  for (let i = 0; i < staleIds.length; i += BATCH) {
    const batch = staleIds.slice(i, i + BATCH);
    execFileSync("npx", ["wrangler", "vectorize", "delete-vectors", INDEX_NAME, "--ids", ...batch], {
      stdio: "inherit",
      shell: IS_WINDOWS,
    });
  }
  console.log("Done.");
}

main();
