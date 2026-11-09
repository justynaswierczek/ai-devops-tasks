
# Simple Task API

## Opis projektu

Simple Task API to prosta aplikacja REST API służąca do zarządzania zadaniami. Projekt został oparty na Node.js, frameworku Express oraz bazie danych MongoDB.

Aplikacja umożliwia tworzenie, przeglądanie, edytowanie i usuwanie zadań, a także filtrowanie ich według statusu i priorytetu.

## Główne funkcjonalności

- Tworzenie nowych zadań.
- Pobieranie listy zadań i szczegółów pojedynczego zadania.
- Aktualizacja istniejących zadań.
- Usuwanie zadań.
- Filtrowanie zadań według statusu i priorytetu.
- Prosta autoryzacja użytkowników.

## Technologie

- **Node.js** – środowisko uruchomieniowe JavaScript.
- **Express** – framework do tworzenia REST API.
- **MongoDB** – baza danych NoSQL.
- **npm** – menedżer pakietów.

## Instalacja

### 1. Pobranie projektu

```bash
git clone <adres-repozytorium>
cd simple-task-api
```

### 2. Instalacja zależności

```bash
npm install
```

### 3. Konfiguracja środowiska

Utwórz plik `.env` i uzupełnij dane konfiguracyjne.

Przykładowa konfiguracja:

```env
PORT=3000
MONGO_URI=mongodb://localhost:27017/simple-task-api
```

Nazwy zmiennych środowiskowych należy dostosować do rzeczywistej implementacji aplikacji.

### 4. Uruchomienie aplikacji

Przykładowe polecenie:

```bash
npm start
```

Zakłada ono, że w pliku `package.json` zdefiniowano odpowiedni skrypt `start`.

## Użycie

Po uruchomieniu aplikacja może być dostępna pod adresem:

`http://localhost:3000`

Do komunikacji z API można wykorzystać Postman, cURL lub inną aplikację obsługującą żądania HTTP.

### Przykład tworzenia zadania

```http
POST /api/tasks HTTP/1.1
Content-Type: application/json

{
  "title": "Przygotować dokumentację",
  "description": "Napisać README projektu",
  "status": "pending",
  "priority": "high"
}
```

## Endpointy API

Poniższa tabela przedstawia przykładową strukturę endpointów REST API.

| Metoda | Endpoint | Opis |
|---|---|---|
| GET | `/api/tasks` | Pobranie listy zadań |
| GET | `/api/tasks/:id` | Pobranie pojedynczego zadania |
| POST | `/api/tasks` | Utworzenie nowego zadania |
| PUT | `/api/tasks/:id` | Aktualizacja zadania |
| DELETE | `/api/tasks/:id` | Usunięcie zadania |
| POST | `/api/auth/login` | Logowanie użytkownika |

### Filtrowanie zadań

Przykładowe żądanie:

```http
GET /api/tasks?status=completed&priority=high
```

Pozwala pobrać zadania o statusie `completed` i priorytecie `high`.

### Przykładowa odpowiedź API

```json
[
  {
    "id": "1",
    "title": "Przygotować dokumentację",
    "description": "Napisać README projektu",
    "status": "completed",
    "priority": "high"
  }
]
```

## Autoryzacja

Projekt zakłada prostą autoryzację użytkowników, która umożliwia kontrolowanie dostępu do wybranych operacji.

Szczegóły mechanizmu autoryzacji, np. wykorzystanie tokenów JWT, zależą od implementacji aplikacji.

## Uwagi

Dokumentacja została przygotowana na podstawie ogólnego opisu projektu.

Przed wykorzystaniem jej w rzeczywistej aplikacji należy sprawdzić zgodność endpointów, sposobu uruchamiania, zmiennych środowiskowych i formatu odpowiedzi z kodem źródłowym.
