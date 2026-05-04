# Add breadcrumb metadata to all files with breadcrumb nav
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
$files = Get-Content 'C:\ZZZWebsites\cmlocals\breadcrumb-files.txt'

foreach ($relativePath in $files) {
  $filePath = "C:\ZZZWebsites\cmlocals\pages$relativePath"

  if (Test-Path $filePath) {
    $content = Get-Content $filePath -Raw

    # Skip if already has metadata
    if ($content -match 'breadcrumb-meta.*Read time') {
      continue
    }

    # Find the closing breadcrumb tag and add metadata before it
    # Look for pattern: </div> followed by </nav> or close to </nav>
    if ($content -match '</div>\s*</nav>' -or $content -match '(?<!</div>)\s*</nav>') {
      # This handles both cases where breadcrumb-inner is closed or not
      $newContent = $content -replace '(</div>)\s*(</nav>)', "`n$metadata`n`$1`n`$2"

      if ($newContent -ne $content) {
        # Add CSS if not present
        if ($newContent -notmatch '\.breadcrumb-meta\s*\{') {
          $newContent = $newContent -replace '(</style>)', "`n$cssRule`n`$1"
        }

        # Add script if not present (only for article pages)
        if ($newContent -match 'article.*class="article-body"' -and $newContent -notmatch 'calculateReadTime') {
          $newContent = $newContent -replace '(<script src="[^"]*progress-bar\.js")', "$readTimeScript`n`n`$1"
        }

        Set-Content -Path $filePath -Value $newContent -Encoding UTF8
        $processed++
      }
    }
  }
}

Write-Output "Updated $processed pages"
