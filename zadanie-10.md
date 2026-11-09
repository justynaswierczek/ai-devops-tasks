
# Zadanie 10: Generowanie prostego pliku .gitignore

## Cel zadania

Celem zadania jest wygenerowanie pliku `.gitignore` dla projektu Node.js wykorzystującego Docker oraz lokalną bazę danych MongoDB.

## Prompt 1

Stwórz plik .gitignore dla projektu Node.js, który używa Docker i przechowuje dane w lokalnej bazie MongoDB.

## Wygenerowany plik .gitignore

Wygenerowaną konfigurację zapisano w osobnym pliku `.gitignore` w repozytorium.

Plik zawiera reguły ignorowania:
- Zależności Node.js (`node_modules/`).
- Logów aplikacji (`*.log`).
- Plików tymczasowych i pamięci podręcznej.
- Plików środowiskowych (`.env`).
- Plików kompilacji (`dist/`, `build/`).
- Lokalnej konfiguracji Docker Compose.
- Danych i kopii zapasowych MongoDB.
- Plików systemowych oraz ustawień edytorów kodu.

## Prompt 2

Dlaczego ważne jest ignorowanie tych plików?

## Odpowiedź ChatGPT

Ignorowanie wybranych plików za pomocą `.gitignore` jest ważne z kilku powodów.

**1. Ochrona poufnych danych**

Pliki `.env` mogą zawierać hasła, klucze API i dane dostępowe do bazy danych. Dodanie ich do `.gitignore` zmniejsza ryzyko przypadkowego przesłania tych informacji do repozytorium.

**2. Zmniejszenie rozmiaru repozytorium**

Folder `node_modules/` zawiera biblioteki instalowane przez npm. Nie trzeba ich przechowywać w Git, ponieważ można je ponownie zainstalować za pomocą `npm install` lub `npm ci`.

**3. Unikanie niepotrzebnych plików**

Logi, pliki tymczasowe i pamięć podręczna są generowane automatycznie podczas działania aplikacji. Ich zapisywanie w repozytorium powodowałoby niepotrzebne zmiany.

**4. Ochrona lokalnych danych MongoDB**

Foldery zawierające lokalne dane bazy MongoDB oraz kopie zapasowe nie powinny być przypadkowo dodawane do repozytorium. Mogą zajmować dużo miejsca i zawierać poufne informacje.

**5. Zachowanie porządku w projekcie**

Ignorowanie plików generowanych przez system operacyjny i edytory kodu pozwala utrzymać repozytorium w czystości.

**6. Ułatwienie pracy zespołowej**

Dzięki `.gitignore` do repozytorium trafiają przede wszystkim pliki potrzebne do rozwoju aplikacji. Ogranicza to liczbę niepotrzebnych zmian i konfliktów.

## Wnioski i obserwacje

Plik `.gitignore` pomaga utrzymać porządek w repozytorium oraz ogranicza ryzyko przypadkowego udostępnienia poufnych danych.

W projektach Node.js korzystających z Docker i MongoDB szczególnie ważne jest ignorowanie zależności, plików środowiskowych, logów oraz lokalnych danych bazy.

AI pozwoliło szybko przygotować przykładową konfigurację i wyjaśniło znaczenie poszczególnych reguł.
