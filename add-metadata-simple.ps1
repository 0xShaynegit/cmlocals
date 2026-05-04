# Simple non-regex approach

$metadata = '  <span class="breadcrumb-sep" aria-hidden="true">·</span>' + "`n" + '  <span class="breadcrumb-meta">Read time: <span id="read-time">7 min</span></span>' + "`n" + '  <span class="breadcrumb-sep" aria-hidden="true">·</span>' + "`n" + '  <span class="breadcrumb-meta">Last updated: February 2026</span>'

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
  if ($content.Contains('class="breadcrumb"') -and -not $content.Contains('breadcrumb-meta')) {

    # Find </div></nav> pattern and insert metadata before it
    $searchString = '</div>' + "`n" + '</nav>'
    $replaceString = "`n$metadata`n" + '</div>' + "`n" + '</nav>'

    if ($content.Contains($searchString)) {
      $newContent = $content.Replace($searchString, $replaceString)

      # Add CSS if missing
      if (-not $newContent.Contains('.breadcrumb-meta {')) {
        $cssSearchString = '</style>'
        $cssReplaceString = "`n$cssRule`n" + '</style>'
        $newContent = $newContent.Replace($cssSearchString, $cssReplaceString)
      }

      # Add script if missing (only for article pages)
      if ($newContent.Contains('article') -and $newContent.Contains('article-body') -and -not $newContent.Contains('calculateReadTime')) {
        $scriptSearchString = '<script src="../../shared/js/progress-bar.js" defer></script>'
        $scriptReplaceString = $readTimeScript + "`n`n" + $scriptSearchString
        if ($newContent.Contains($scriptSearchString)) {
          $newContent = $newContent.Replace($scriptSearchString, $scriptReplaceString)
        }
      }

      Set-Content -Path $filePath -Value $newContent -Encoding UTF8
      $processed++
    }
  }
}

Write-Output "Completed: Updated $processed pages"
