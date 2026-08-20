# Ежедневный запуск Job Scout. Вешается на Планировщик задач Windows.
$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

$log = Join-Path $PSScriptRoot "data\run.log"
"=== $(Get-Date -Format 'yyyy-MM-dd HH:mm') ===" | Out-File -FilePath $log -Append -Encoding utf8

try {
    py -m scout run --drafts 3 2>&1 | Tee-Object -FilePath $log -Append

    $today  = Get-Date -Format "yyyy-MM-dd"
    $digest = Join-Path $PSScriptRoot "data\digests\$today.md"
    if (Test-Path $digest) { Invoke-Item $digest }
}
catch {
    "ОШИБКА: $_" | Out-File -FilePath $log -Append -Encoding utf8
    throw
}
