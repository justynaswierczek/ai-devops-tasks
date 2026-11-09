
# Zadanie 5: Wizualizacja ASCII Art

## Cel zadania

Celem zadania jest stworzenie prostego diagramu ASCII Art przedstawiającego połączenie klienta, serwera aplikacji i bazy danych, a następnie jego ulepszenie poprzez dodanie opisów i kierunków przepływu danych.

## Diagram 1: Podstawowa wizualizacja

**Prompt:**

Stwórz prosty diagram ASCII Art przedstawiający połączenie klienta, serwera aplikacji i bazy danych.

**Odpowiedź ChatGPT:**

```text
+------------+       +-------------------+       +--------------+
|   Klient   | ----> | Serwer aplikacji  | ----> | Baza danych  |
+------------+       +-------------------+       +--------------+
```

Diagram przedstawia podstawową architekturę systemu, w której klient komunikuje się z serwerem aplikacji, a serwer korzysta z bazy danych.

## Diagram 2: Ulepszona wizualizacja

**Prompt:**

Dodaj do diagramu opisy elementów i kierunki przepływu danych.

**Odpowiedź ChatGPT:**

```text
+--------------------+
|       KLIENT       |
| Przeglądarka WWW   |
| Interfejs użytk.   |
+--------------------+
          |
          | Żądanie HTTP/HTTPS
          v
+--------------------+
|  SERWER APLIKACJI  |
| Logika biznesowa   |
| Obsługa żądań API  |
+--------------------+
          |
          | Zapytanie SQL
          v
+--------------------+
|    BAZA DANYCH     |
| Przechowywanie     |
| i odczyt danych    |
+--------------------+
          |
          | Wynik zapytania
          v
+--------------------+
|  SERWER APLIKACJI  |
| Przetwarzanie      |
| odpowiedzi         |
+--------------------+
          |
          | Odpowiedź HTTP/HTTPS
          v
+--------------------+
|       KLIENT       |
| Wyświetlenie       |
| wyników            |
+--------------------+
```

Ulepszony diagram przedstawia pełny przepływ danych. Klient wysyła żądanie HTTP/HTTPS do serwera aplikacji. Serwer przetwarza żądanie i komunikuje się z bazą danych za pomocą SQL. Baza zwraca wyniki do serwera, który następnie przesyła odpowiedź do klienta.

## Porównanie diagramów

Pierwszy diagram jest prosty i przedstawia jedynie trzy główne elementy systemu oraz ich połączenia. Pozwala szybko zrozumieć podstawową architekturę aplikacji.

Drugi diagram jest bardziej szczegółowy. Zawiera opisy funkcji poszczególnych elementów oraz pokazuje kierunki przepływu danych, w tym wysyłanie żądań i zwracanie odpowiedzi.

## Wnioski i obserwacje

AI potrafi generować proste diagramy ASCII Art bez używania dodatkowych narzędzi graficznych. Doprecyzowanie promptu pozwoliło uzyskać bardziej czytelną i szczegółową wizualizację.

Drugi diagram lepiej przedstawia sposób komunikacji pomiędzy klientem, serwerem aplikacji i bazą danych, dzięki czemu jest bardziej przydatny do wyjaśniania działania systemu.
