// Cloudflare Pages Function: POST /api/chat
// Retrieves relevant page chunks from Vectorize, then asks a Workers AI chat
// model to answer using only that context.

const EMBED_MODEL = "@cf/baai/bge-base-en-v1.5";
const CHAT_MODEL = "@cf/meta/llama-3.1-8b-instruct";
const TOP_K = 5;

export async function onRequestPost(context) {
  const { request, env } = context;

  let body;
  try {
    body = await request.json();
  } catch {
    return jsonResponse({ error: "Invalid JSON body" }, 400);
  }

  const question = (body.question || "").toString().trim().slice(0, 1000);
  if (!question) {
    return jsonResponse({ error: "Missing 'question'" }, 400);
  }

  const embedded = await env.AI.run(EMBED_MODEL, { text: [question] });
  const vector = embedded.data[0];

  const matches = await env.VECTOR_INDEX.query(vector, {
    topK: TOP_K,
    returnMetadata: true,
  });

  const contextChunks = matches.matches
    .filter((m) => m.score > 0.4)
    .map((m) => m.metadata);

  if (contextChunks.length === 0) {
    return jsonResponse({
      answer:
        "I couldn't find anything about that on CMLocals. Try rephrasing, or browse the visa guides directly.",
      sources: [],
    });
  }

  const contextText = contextChunks
    .map((c, i) => `[${i + 1}] (${c.url}) ${c.title}\n${c.text}`)
    .join("\n\n");

  const systemPrompt = `You are the CMLocals website assistant. CMLocals is a Chiang Mai / Thailand visa and immigration guide site. Answer the user's question using ONLY the context below, which is pulled from the site's own pages. If the context doesn't contain the answer, say you don't have that information on the site and suggest they check the relevant guide page. Keep answers concise (2-5 sentences). Cite the page URL(s) you used in parentheses at the end.

Context:
${contextText}`;

  const chatResult = await env.AI.run(CHAT_MODEL, {
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: question },
    ],
    max_tokens: 400,
  });

  const uniqueSources = [...new Map(contextChunks.map((c) => [c.url, c.title])).entries()].map(
    ([url, title]) => ({ url, title })
  );

  return jsonResponse({
    answer: chatResult.response,
    sources: uniqueSources,
  });
}

export async function onRequestOptions() {
  return new Response(null, { headers: corsHeaders() });
}

function corsHeaders() {
  return {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };
}

function jsonResponse(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", ...corsHeaders() },
  });
}
