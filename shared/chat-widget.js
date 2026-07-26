(function () {
  const STYLE = `
  #cml-chat-btn{position:fixed;bottom:20px;right:20px;z-index:9999;width:56px;height:56px;border-radius:50%;
    background:#0d6b4f;color:#fff;border:none;box-shadow:0 4px 14px rgba(0,0,0,.25);cursor:pointer;font-size:24px}
  #cml-chat-panel{position:fixed;bottom:88px;right:20px;z-index:9999;width:340px;max-width:90vw;height:460px;
    max-height:70vh;background:#fff;border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,.25);
    display:none;flex-direction:column;overflow:hidden;font-family:system-ui,sans-serif}
  #cml-chat-panel.open{display:flex}
  #cml-chat-head{background:#0d6b4f;color:#fff;padding:12px 14px;font-weight:600;font-size:14px}
  #cml-chat-log{flex:1;overflow-y:auto;padding:12px;font-size:13px;line-height:1.45;color:#222}
  .cml-msg{margin-bottom:10px;padding:8px 10px;border-radius:8px;max-width:88%}
  .cml-msg.user{background:#e9f5f0;margin-left:auto}
  .cml-msg.bot{background:#f2f2f2;margin-right:auto}
  .cml-msg a{color:#0d6b4f}
  #cml-chat-form{display:flex;border-top:1px solid #eee}
  #cml-chat-input{flex:1;border:none;padding:10px;font-size:13px;outline:none}
  #cml-chat-form button{border:none;background:#0d6b4f;color:#fff;padding:0 14px;cursor:pointer}
  `;

  const style = document.createElement("style");
  style.textContent = STYLE;
  document.head.appendChild(style);

  const btn = document.createElement("button");
  btn.id = "cml-chat-btn";
  btn.setAttribute("aria-label", "Open chat");
  btn.textContent = "💬";

  const panel = document.createElement("div");
  panel.id = "cml-chat-panel";
  panel.innerHTML = `
    <div id="cml-chat-head">Ask CMLocals</div>
    <div id="cml-chat-log"></div>
    <form id="cml-chat-form">
      <input id="cml-chat-input" type="text" placeholder="Ask about visas, ED programs..." autocomplete="off" />
      <button type="submit">Send</button>
    </form>
  `;

  document.body.appendChild(btn);
  document.body.appendChild(panel);

  const log = panel.querySelector("#cml-chat-log");
  const form = panel.querySelector("#cml-chat-form");
  const input = panel.querySelector("#cml-chat-input");

  function addMessage(text, role) {
    const div = document.createElement("div");
    div.className = "cml-msg " + role;
    div.innerHTML = text;
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
  }

  let greeted = false;
  btn.addEventListener("click", () => {
    panel.classList.toggle("open");
    if (!greeted) {
      addMessage("Hi! Ask me anything about Thai visas, ED programs, or Chiang Mai life on CMLocals.", "bot");
      greeted = true;
    }
  });

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const question = input.value.trim();
    if (!question) return;
    addMessage(escapeHtml(question), "user");
    input.value = "";
    const loadingId = "loading-" + Date.now();
    addMessage('<span id="' + loadingId + '">Thinking...</span>', "bot");

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const data = await res.json();
      const loadingEl = document.getElementById(loadingId);
      const sourcesHtml = (data.sources || [])
        .map((s) => `<a href="${s.url}">${escapeHtml(s.title)}</a>`)
        .join("<br>");
      loadingEl.parentElement.innerHTML =
        escapeHtml(data.answer || "Sorry, something went wrong.") +
        (sourcesHtml ? "<br><br><small>" + sourcesHtml + "</small>" : "");
    } catch (err) {
      const loadingEl = document.getElementById(loadingId);
      loadingEl.parentElement.textContent = "Sorry, the chat is unavailable right now.";
    }
  });

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }
})();
