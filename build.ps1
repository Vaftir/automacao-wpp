$exclude = @("venv", "botyago.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "botyago.zip" -Force