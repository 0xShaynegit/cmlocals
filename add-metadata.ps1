# Add breadcrumb metadata to all article pages
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
Push-Location C:\ZZZWebsites\cmlocals\pages

Get-ChildItem -Path . -Filter '*.html' -Recurse | Where-Object { $_.Name -ne 'index.html' } | ForEach-Object {
  $filePath = $_.FullName
  $content = Get-Content $filePath -Raw

  # Only process if has article.article-body and breadcrumb nav
  if ($content -match 'article.*class="article-body"' -and $content -match '<nav[^>]*breadcrumb') {
    # Add metadata before closing breadcrumb if not already present
    if ($content -notmatch 'breadcrumb-meta.*Read time') {
      $content = $content -replace '(</div>)(\s*</nav>)', "`n$metadata`n`$1`n`$2"
    }

    # Add CSS rule before </style> if not present
    if ($content -notmatch '\.breadcrumb-meta') {
      $content = $content -replace '(</style>)', "`n$cssRule`n`$1"
    }

    # Add calculateReadTime script if not present
    if ($content -notmatch 'calculateReadTime') {
      $content = $content -replace '(<script src="[^"]*progress-bar\.js")', "$readTimeScript`n`n`$1"
    }

    Set-Content -Path $filePath -Value $content -Encoding UTF8
    $processed++
  }
}

Pop-Location
Write-Output "Updated $processed pages"
