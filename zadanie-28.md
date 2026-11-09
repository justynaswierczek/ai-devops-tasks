
# Zadanie 28: Skrypt do zarządzania zadaniami Jenkins

## Cel zadania

Celem zadania jest wykorzystanie AI do wygenerowania skryptu Python umożliwiającego zarządzanie zadaniami Jenkins za pomocą REST API.

Skrypt pozwala wyświetlać listę zadań, sprawdzać status ostatniego buildu oraz uruchamiać wybrane zadanie.

## Prompt 1

Napisz skrypt w Pythonie, który używa Jenkins API do:
- listowania wszystkich zadań (jobs)
- sprawdzania statusu ostatnich buildów
- uruchamiania wybranego zadania

Uwzględnij obsługę autoryzacji i obsługę błędów.

## Wygenerowany skrypt

Skrypt został zapisany w pliku `jenkins-manager.py`.

Do komunikacji z Jenkins REST API wykorzystano bibliotekę `requests`.

## Prompt 2

Wyjaśnij, jak działa ten skrypt i jakich bibliotek używa do komunikacji z Jenkins API. Podaj również przykładowe polecenia, jak używać tego skryptu.

## Wyjaśnienie działania skryptu

### 1. Import bibliotek

```python
import os
import sys
import argparse
import requests
from urllib.parse import quote
```

Skrypt wykorzystuje następujące biblioteki:

- `os` – pobieranie zmiennych środowiskowych.
- `sys` – zakończenie programu z odpowiednim kodem.
- `argparse` – obsługa argumentów podawanych w terminalu.
- `requests` – wysyłanie zapytań HTTP do Jenkins API.
- `urllib.parse` – kodowanie nazw zadań w adresach URL.

Biblioteki `os`, `sys`, `argparse` i `urllib.parse` należą do standardowej biblioteki Pythona.

Bibliotekę `requests` należy zainstalować osobno.

### 2. Konfiguracja połączenia

```python
JENKINS_URL = os.getenv("JENKINS_URL", "http://localhost:8080").rstrip("/")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")
```

Skrypt odczytuje adres serwera Jenkins, nazwę użytkownika oraz token API ze zmiennych środowiskowych.

Dzięki temu dane logowania nie muszą być wpisywane bezpośrednio w kodzie.

### 3. Autoryzacja

```python
session = requests.Session()

if JENKINS_USER and JENKINS_TOKEN:
    session.auth = (JENKINS_USER, JENKINS_TOKEN)
```

Wykorzystano uwierzytelnianie HTTP Basic Auth z nazwą użytkownika i tokenem Jenkins API.

Obiekt `Session` umożliwia ponowne wykorzystanie konfiguracji połączenia.

### 4. Obsługa błędów

Funkcja `api_request()` odpowiada za wysyłanie zapytań HTTP.

Obsługuje między innymi:

- Błędy HTTP, np. 401, 403 i 404.
- Brak połączenia z serwerem Jenkins.
- Przekroczenie czasu oczekiwania.
- Inne błędy komunikacji HTTP.

Dzięki temu program wyświetla komunikat zamiast kończyć działanie nieobsłużonym wyjątkiem sieciowym.

### 5. Listowanie zadań

Funkcja `get_jobs()` wysyła zapytanie GET do endpointu:

`/api/json?tree=jobs[name,color]`

Jenkins zwraca listę zadań wraz z ich nazwami i informacjami o stanie.

Skrypt wyświetla zadania w terminalu.

### 6. Sprawdzanie statusu buildu

Funkcja `get_last_build(job_name)` pobiera informacje o ostatnim buildzie wskazanego zadania.

Wyświetlane są:

- Nazwa zadania.
- Numer ostatniego buildu.
- Wynik, np. SUCCESS lub FAILURE.
- Informacja, czy build nadal trwa.
- Adres URL buildu.

### 7. Uruchamianie zadania

Funkcja `run_job(job_name)` wysyła zapytanie POST do endpointu:

`/job/nazwa-zadania/build`

Powoduje to zlecenie uruchomienia wskazanego zadania.

Poprawna odpowiedź serwera oznacza przyjęcie żądania, a nie zakończenie buildu sukcesem.

### 8. Obsługa poleceń

Biblioteka `argparse` umożliwia wybór działania skryptu za pomocą argumentów w terminalu.

Dostępne polecenia:

- `list` – wyświetlenie listy zadań.
- `status` – sprawdzenie ostatniego buildu.
- `run` – uruchomienie zadania.

## Instalacja i konfiguracja

### Instalacja biblioteki requests

```bash
pip install requests
```

### Konfiguracja zmiennych środowiskowych

Przykład dla PowerShell w systemie Windows:

```powershell
$env:JENKINS_URL = "http://localhost:8080"
$env:JENKINS_USER = "admin"
$env:JENKINS_TOKEN = "TWOJ_TOKEN_API"
```

Token API można wygenerować w ustawieniach konta użytkownika Jenkins.

Nie należy umieszczać prawdziwego tokenu w repozytorium Git.

W przypadku połączenia z serwerem zdalnym należy korzystać z HTTPS.

## Przykładowe polecenia

### 1. Wyświetlenie wszystkich zadań

```bash
python jenkins-manager.py list
```

Przykładowy wynik:

```text
Lista zadan Jenkins:
- Build-App (status: blue)
- Test-App (status: red)
- Deploy-App (status: blue)
```

### 2. Sprawdzenie statusu ostatniego buildu

```bash
python jenkins-manager.py status Build-App
```

Przykładowy wynik:

```text
Zadanie: Build-App
Numer buildu: 15
Wynik: SUCCESS
Czy trwa: False
URL: http://localhost:8080/job/Build-App/15/
```

### 3. Uruchomienie wybranego zadania

```bash
python jenkins-manager.py run Build-App
```

Przykładowy wynik:

```text
Zlecono uruchomienie zadania: Build-App
```

## Najlepsze praktyki

1. Przechowywanie tokenów API w zmiennych środowiskowych zamiast w kodzie.
2. Stosowanie HTTPS podczas komunikacji z serwerem Jenkins.
3. Obsługa błędów HTTP i problemów z połączeniem.
4. Ograniczenie uprawnień użytkownika API do niezbędnego minimum.
5. Ustawianie limitów czasu dla zapytań HTTP.
6. Niewysyłanie danych logowania do publicznych repozytoriów.

## Wnioski i obserwacje

AI wygenerowało skrypt Python wykorzystujący Jenkins REST API do zarządzania zadaniami.

Skrypt umożliwia pobieranie listy zadań, sprawdzanie wyników ostatnich buildów oraz zlecanie uruchomienia wybranego zadania.

Zastosowanie biblioteki `requests` upraszcza komunikację HTTP, a `argparse` pozwala wygodnie obsługiwać program z terminala.

Zadanie pokazało, że Jenkins może być zarządzany nie tylko przez interfejs graficzny, ale również programowo za pomocą API.

Przed użyciem skryptu w rzeczywistym środowisku należy skonfigurować połączenie z serwerem Jenkins i odpowiednie uprawnienia użytkownika.
