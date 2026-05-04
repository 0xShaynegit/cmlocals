# Fix garbled encoding issues in all HTML files

$dir = 'C:\ZZZWebsites\cmlocals\pages'
$fixed = 0

Get-ChildItem -Path $dir -Filter '*.html' -Recurse | ForEach-Object {
  $filePath = $_.FullName
  $content = Get-Content $filePath -Raw -Encoding UTF8

  # Replace garbled em dash "â€"" with proper em dash or hyphen
  if ($content -match 'â€"') {
    $newContent = $content -replace 'â€"', ' - '

    Set-Content -Path $filePath -Value $newContent -Encoding UTF8
    $fixed++
  }
}

Write-Output "Fixed encoding in $fixed files"
