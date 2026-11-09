
# Zadanie 16: Konwersja Bash do PowerShell

## Cel zadania

Celem zadania jest przekonwertowanie skryptu Bash służącego do tworzenia kopii zapasowej bazy danych MySQL na równoważny skrypt PowerShell dla systemu Windows.

## Prompt

Przekonwertuj ten skrypt bash na równoważny skrypt PowerShell dla Windows.

## Oryginalny skrypt Bash

Oryginalny skrypt zapisano w pliku `backup-db.sh`.

Skrypt wykonuje kopię zapasową bazy danych `app_database` za pomocą narzędzia `mysqldump`, a następnie kompresuje ją do formatu GZip.

Przed rozpoczęciem sprawdza, czy katalog na kopie zapasowe istnieje. Jeśli nie, automatycznie go tworzy.

## Skrypt PowerShell

Przekonwertowany skrypt zapisano w pliku `backup-db.ps1`.

Skrypt wykonuje te same podstawowe operacje:
1. Definiuje nazwę bazy danych i katalog backupu.
2. Generuje nazwę pliku zawierającą aktualną datę i godzinę.
3. Sprawdza istnienie katalogu i w razie potrzeby go tworzy.
4. Wykonuje eksport bazy danych za pomocą `mysqldump.exe`.
5. Kompresuje plik SQL do formatu GZip.
6. Wyświetla komunikat o powodzeniu lub błędzie.

## Główne różnice między Bash a PowerShell

**1. Deklarowanie zmiennych**

W Bash zmienne zapisuje się bez znaku `$` przy przypisywaniu:

```bash
DB_NAME="app_database"
```

W PowerShell nazwa zmiennej zawsze zaczyna się od `$`:

```powershell
$DB_NAME = "app_database"
```

**2. Pobieranie aktualnej daty**

Bash:

```bash
DATE=$(date +%Y%m%d_%H%M%S)
```

PowerShell:

```powershell
$DATE = Get-Date -Format "yyyyMMdd_HHmmss"
```

Oba polecenia generują datę i godzinę, które można wykorzystać w nazwie pliku.

**3. Sprawdzanie istnienia katalogu**

Bash:

```bash
if [ ! -d "$BACKUP_DIR" ]; then
```

PowerShell:

```powershell
if (-not (Test-Path $BACKUP_DIR)) {
```

W Bash używa się operatora `-d`, natomiast w PowerShell polecenia `Test-Path`.

**4. Tworzenie katalogu**

Bash:

```bash
mkdir -p "$BACKUP_DIR"
```

PowerShell:

```powershell
New-Item -ItemType Directory -Path $BACKUP_DIR -Force
```

Oba polecenia pozwalają utworzyć katalog, jeśli wcześniej nie istniał.

**5. Wyświetlanie komunikatów**

W Bash używa się `echo`, natomiast w PowerShell można zastosować `Write-Host`.

**6. Kompresowanie plików**

W Bash wykorzystano polecenie `gzip`, które kompresuje wynik eksportu bazy danych.

W PowerShell wykorzystano klasę `.NET GZipStream`, która umożliwia kompresję pliku do formatu GZip.

**7. Obsługa błędów**

W Bash sprawdzany jest kod zakończenia ostatniego polecenia za pomocą `$?`.

W PowerShell zastosowano `$LASTEXITCODE` do sprawdzenia wyniku działania `mysqldump.exe` oraz konstrukcję `try/catch` do obsługi błędów.

**8. Ścieżki do plików**

Bash korzysta ze ścieżek charakterystycznych dla systemu Linux, np. `/var/backups/db`.

PowerShell w systemie Windows wykorzystuje ścieżki takie jak `C:\Backups\db`.

## Porównanie skryptów

| Cecha | Bash | PowerShell |
|---|---|---|
| System | Linux | Windows |
| Zmienne | `DB_NAME` | `$DB_NAME` |
| Data | `date` | `Get-Date` |
| Sprawdzanie katalogu | `-d` | `Test-Path` |
| Tworzenie katalogu | `mkdir -p` | `New-Item` |
| Komunikaty | `echo` | `Write-Host` |
| Kompresja | `gzip` | `.NET GZipStream` |
| Obsługa błędów | Kod zakończenia | `$LASTEXITCODE`, `try/catch` |

## Wnioski i obserwacje

Oba skrypty realizują ten sam cel, czyli utworzenie skompresowanej kopii zapasowej bazy danych MySQL.

Największe różnice dotyczą składni zmiennych, sposobu wykonywania poleceń systemowych, obsługi błędów oraz kompresji plików.

PowerShell wykorzystuje polecenia i obiekty .NET, natomiast Bash opiera się głównie na poleceniach systemowych i potokach.

AI pomogło przekształcić skrypt do postaci odpowiedniej dla Windows, zachowując jego podstawową funkcjonalność.
