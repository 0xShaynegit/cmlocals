# Remove breadcrumb nav from all checklist pages with multiline support

$dir = 'C:\ZZZWebsites\cmlocals\pages\checklists'
$removed = 0

Get-ChildItem -Path $dir -Filter '*.html' | Where-Object { $_.Name -ne 'index.html' } | ForEach-Object {
  $filePath = $_.FullName
  $content = Get-Content $filePath -Raw

  # Remove breadcrumb section with multiline pattern support
  if ($content -match '<nav class="breadcrumb">' ) {
    $newContent = $content -replace '(?s)<nav class="breadcrumb">.*?</nav>\s*', ''

    if ($newContent -ne $content) {
      Set-Content -Path $filePath -Value $newContent -Encoding UTF8
      Write-Output "Removed breadcrumb from: $($_.Name)"
      $removed++
    }
  }
}

Write-Output "`nCompleted: Removed breadcrumbs from $removed checklist files"
