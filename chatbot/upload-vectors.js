// Embeds content-chunks.json via Workers AI and inserts into a Vectorize index.
// Requires env vars: CLOUDFLARE_ACCOUNT_ID, CLOUDFLARE_API_TOKEN
// Usage: node chatbot/upload-vectors.js [--index=cmlocals-content] [--create]

const fs = require("fs");
const path = require("path");

const ACCOUNT_ID = process.env.CLOUDFLARE_ACCOUNT_ID;
const API_TOKEN = process.env.CLOUDFLARE_API_TOKEN;
const EMBED_MODEL = "@cf/baai/bge-base-en-v1.5"; // 768 dims
const BATCH_SIZE = 50;

const args = Object.fromEntries(
  process.argv.slice(2).map((a) => {
    const [k, v] = a.replace(/^--/, "").split("=");
    return [k, v ?? true];
  })
);
const INDEX_NAME = args.index || "cmlocals-content";

if (!ACCOUNT_ID || !API_TOKEN) {
  console.error("Set CLOUDFLARE_ACCOUNT_ID and CLOUDFLARE_API_TOKEN env vars first.");
  process.exit(1);
}

async function cfFetch(urlPath, opts = {}) {
  const res = await fetch(`https://api.cloudflare.com${urlPath}`, {
    ...opts,
    headers: {
      Authorization: `Bearer ${API_TOKEN}`,
      "Content-Type": "application/json",
      ...(opts.headers || {}),
    },
  });
  const json = await res.json();
  if (!res.ok || json.success === false) {
    throw new Error(`Cloudflare API error (${res.status}): ${JSON.stringify(json.errors || json)}`);
  }
  return json;
}

async function embedBatch(texts) {
  const json = await cfFetch(
    `/client/v4/accounts/${ACCOUNT_ID}/ai/run/${EMBED_MODEL}`,
    { method: "POST", body: JSON.stringify({ text: texts }) }
  );
  return json.result.data; // array of vectors
}

async function main() {
  const chunksPath = path.join(__dirname, "content-chunks.json");
  const chunks = JSON.parse(fs.readFileSync(chunksPath, "utf8"));
  console.log(`Embedding ${chunks.length} chunks with ${EMBED_MODEL}...`);

  const ndjsonLines = [];
  for (let i = 0; i < chunks.length; i += BATCH_SIZE) {
    const batch = chunks.slice(i, i + BATCH_SIZE);
    const vectors = await embedBatch(batch.map((c) => c.text));
    batch.forEach((c, j) => {
      ndjsonLines.push(
        JSON.stringify({
          id: c.id,
          values: vectors[j],
          metadata: { url: c.url, title: c.title, text: c.text.slice(0, 800) },
        })
      );
    });
    console.log(`  embedded ${Math.min(i + BATCH_SIZE, chunks.length)}/${chunks.length}`);
  }

  const outFile = path.join(__dirname, "vectors.ndjson");
  fs.writeFileSync(outFile, ndjsonLines.join("\n") + "\n");
  console.log(`Wrote ${ndjsonLines.length} vectors -> ${outFile}`);
  console.log(`\nNow run:`);
  console.log(`  npx wrangler vectorize insert ${INDEX_NAME} --file=chatbot/vectors.ndjson`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
