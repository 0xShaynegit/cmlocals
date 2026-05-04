# Fix unclosed breadcrumb divs in all checklist pages

$checklistDir = 'C:\ZZZWebsites\cmlocals\pages\checklists'
$fixed = 0

Get-ChildItem -Path $checklistDir -Filter '*.html' | ForEach-Object {
  $filePath = $_.FullName
  $content = Get-Content $filePath -Raw

  # Look for: </span> followed by blank lines and then <!-- (breadcrumb not properly closed)
  if ($content -match '</span>\s*\n\s*\n<!--' -and $content -notmatch '</span>\s*\n</div>\s*\n</nav>') {
    # Replace the pattern: </span> newlines <!--
    # With: </span> newline </div> newline </nav> newlines <!--
    $newContent = $content -replace '(</span>)\s*(\n\s*\n)(<!--)', "`$1`n</div>`n</nav>`n`n`$3"

    Set-Content -Path $filePath -Value $newContent -Encoding UTF8
    Write-Output "Fixed: $($_.Name)"
    $fixed++
  }
}

Write-Output "Completed: Fixed $fixed checklist files"
