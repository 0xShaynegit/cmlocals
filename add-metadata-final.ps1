# Direct approach: find all files with breadcrumb and add metadata

$metadata = @'
  <span class="breadcrumb-sep" aria-hidden="true">·</span>
  <span class="breadcrumb-meta">Read time: <span id="read-time">7 min</span></span>
  <span class="breadcrumb-sep" aria-hidden="true">·</span>
  <span class="breadcrumb-meta">Last updated: February 2026</span>
'@

$cssRule = '.breadcrumb-meta { color: var(--c-muted); }'

$readTimeScript = @'

<script>
(function() {
  'use strict';
  function calculateReadTime() {
    const article = document.querySelector('article.article-body');
    if (!article) return;
    const text = article.innerText;
    const wordCount = text.trim().split(/\s+/).length;
    const readTime = Math.max(1, Math.round(wordCount / 200));
    const readTimeEl = document.getElementById('read-time');
    if (readTimeEl) {
      readTimeEl.textContent = readTime + ' min';
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', calculateReadTime);
  } else {
    calculateReadTime();
  }
})();
</script>
'@

$processed = 0

Get-ChildItem -Path 'C:\ZZZWebsites\cmlocals\pages' -Filter '*.html' -Recurse | Where-Object { $_.Name -ne 'index.html' } | ForEach-Object {
  $filePath = $_.FullName
  $content = Get-Content $filePath -Raw

  # Check if file has breadcrumb and skip if already updated
  if ($content -match 'class="breadcrumb"' -and $content -notmatch 'breadcrumb-meta.*Read time') {
    # Add metadata before closing breadcrumb div
    $newContent = $content -replace '(</div>)(\s*</nav>)', ("`n$metadata`n`$1`n`$2")

    if ($newContent -ne $content) {
      # Add CSS if missing
      if ($newContent -notmatch '\.breadcrumb-meta\s*\{') {
        $newContent = $newContent -replace '(</style>)', ("`n$cssRule`n`$1")
      }

      # Add script if missing (only for article pages)
      if ($newContent -match 'article.*class="article-body"' -and $newContent -notmatch 'calculateReadTime') {
        $newContent = $newContent -replace '(<script src="[^"]*progress-bar\.js")', ($readTimeScript + "`n`n`$1")
      }

      Set-Content -Path $filePath -Value $newContent -Encoding UTF8
      $processed++
    }
  }
}

Write-Output "Completed: Updated $processed pages"
