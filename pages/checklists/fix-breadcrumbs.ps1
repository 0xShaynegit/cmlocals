# Fix corrupted breadcrumb HTML in all remaining checklist files

$files = @(
    'ed-visa-checklist.html',
    'marriage-visa-checklist.html',
    're-entry-permit-checklist.html',
    'retirement-visa-checklist.html',
    'tourist-visa-checklist.html',
    'visa-exempt-entry-checklist.html',
    'visa-extension-checklist.html',
    'visa-on-arrival-checklist.html'
)

foreach ($file in $files) {
    $filePath = "C:\ZZZWebsites\cmlocals\pages\checklists\$file"

    if (Test-Path $filePath) {
        $content = Get-Content $filePath -Raw

        # Fix the corrupted pattern: multiple closing tags split across lines
        # Pattern: </div> </nav> <a href... <span>→</span> </div> </nav> <span>Name</span> </div> </nav>
        # Replace with: <a href... <span>→</span> <span>Name</span> </div> </nav>

        # Find the breadcrumb nav section and reconstruct it properly
        if ($content -match '<nav class="breadcrumb">(.*?)<span>→</span>\s*</div>\s*</nav>\s*<a href.*?checklist.*?</a>\s*<span>→</span>\s*</div>\s*</nav>\s*<span>([^<]+)</span>\s*</div>\s*</nav>') {
            # Extract the page name from the third span
            $pageName = $matches[2]

            # Replace the corrupted section with proper HTML
            $content = $content -replace '<nav class="breadcrumb">\s*<div class="breadcrumb-inner">\s*<a href="[^"]*">Home</a>\s*<span>→</span>\s*</div>\s*</nav>\s*<a href="[^"]*">Checklists</a>\s*<span>→</span>\s*</div>\s*</nav>\s*<span>[^<]+</span>\s*</div>\s*</nav>',
                "<nav class=""breadcrumb"">`n<div class=""breadcrumb-inner"">`n  <a href=""../../index.html"">Home</a>`n  <span>→</span>`n  <a href=""../checklists/index.html"">Checklists</a>`n  <span>→</span>`n  <span>$pageName</span>`n</div>`n</nav>"
        }

        Set-Content -Path $filePath -Value $content -Encoding UTF8
        Write-Output "Fixed: $file"
    }
}
