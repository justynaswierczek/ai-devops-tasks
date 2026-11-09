
# Prosty skrypt do backupu bazy danych

$DB_NAME = "app_database"
$BACKUP_DIR = "C:\Backups\db"
$DATE = Get-Date -Format "yyyyMMdd_HHmmss"
$FILENAME = Join-Path $BACKUP_DIR "${DB_NAME}_${DATE}.sql.gz"

# Sprawdź czy katalog istnieje
if (-not (Test-Path $BACKUP_DIR)) {
    New-Item -ItemType Directory -Path $BACKUP_DIR -Force | Out-Null
    Write-Host "Utworzono katalog $BACKUP_DIR"
}

# Wykonaj backup
Write-Host "Rozpoczynam backup bazy $DB_NAME..."

$TEMP_FILE = Join-Path $BACKUP_DIR "${DB_NAME}_${DATE}.sql"

try {
    # Wykonaj eksport bazy do pliku SQL
    & mysqldump.exe -u root -p $DB_NAME > $TEMP_FILE

    if ($LASTEXITCODE -ne 0) {
        throw "Błąd podczas eksportu bazy danych."
    }

    # Skompresuj plik SQL do formatu GZip
    $inputStream = [System.IO.File]::OpenRead($TEMP_FILE)
    try {
        $outputStream = [System.IO.File]::Create($FILENAME)
        try {
            $gzipStream = [System.IO.Compression.GZipStream]::new(
                $outputStream,
                [System.IO.Compression.CompressionMode]::Compress
            )
            try {
                $inputStream.CopyTo($gzipStream)
            }
            finally {
                $gzipStream.Dispose()
            }
        }
        finally {
            $outputStream.Dispose()
        }
    }
    finally {
        $inputStream.Dispose()
    }

    Remove-Item $TEMP_FILE
    Write-Host "Backup zakończony sukcesem: $FILENAME"
}
catch {
    Write-Host "Błąd podczas wykonywania backupu: $_"
    exit 1
}
