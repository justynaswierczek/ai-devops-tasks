
# Dokumentacja API – Lista użytkowników

## Endpoint

`GET /api/users`

## Opis

Endpoint służy do pobierania listy użytkowników. Umożliwia stronicowanie wyników oraz opcjonalne filtrowanie użytkowników według ich roli.

## Parametry zapytania

| Parametr | Typ | Wymagany | Wartość domyślna | Opis |
|---|---|---|---|---|
| `page` | integer | Nie | 1 | Numer strony wyników |
| `limit` | integer | Nie | 10 | Liczba wyników na stronę, maksymalnie 100 |
| `role` | string | Nie | Brak | Filtr użytkowników według roli |

## Przykładowe żądanie

```http
GET /api/users?page=1&limit=10&role=admin HTTP/1.1
Host: example.com
Accept: application/json
```

Żądanie pobiera pierwszą stronę użytkowników z rolą `admin`, z limitem 10 wyników na stronę.

## Przykładowa odpowiedź

**Status HTTP: 200 OK**

```json
{
  "page": 1,
  "limit": 10,
  "total": 2,
  "users": [
    {
      "id": 1,
      "name": "Anna Kowalska",
      "email": "anna@example.com",
      "role": "admin"
    },
    {
      "id": 2,
      "name": "Jan Nowak",
      "email": "jan@example.com",
      "role": "admin"
    }
  ]
}
```

Przedstawiona odpowiedź jest przykładowa. Dokładna struktura danych zależy od implementacji API.

## Przykładowe użycie cURL

```bash
curl "https://example.com/api/users?page=1&limit=10&role=admin"
```

## Możliwe kody odpowiedzi

| Kod HTTP | Znaczenie |
|---|---|
| `200 OK` | Pomyślne pobranie listy użytkowników |
| `400 Bad Request` | Nieprawidłowe parametry zapytania |
| `401 Unauthorized` | Brak wymaganych danych uwierzytelniających |
| `500 Internal Server Error` | Wewnętrzny błąd serwera |

Kody `400`, `401` i `500` są przykładami możliwych odpowiedzi. Ich rzeczywista obsługa wymaga potwierdzenia w implementacji API.

## Uwagi

- Parametr `page` domyślnie przyjmuje wartość `1`.
- Parametr `limit` domyślnie przyjmuje wartość `10` i nie może przekroczyć `100`.
- Parametr `role` jest opcjonalny.
- Jeśli parametr `role` nie zostanie podany, nie jest stosowany filtr według roli.
- Szczegóły walidacji parametrów i format odpowiedzi powinny zostać potwierdzone w kodzie aplikacji.
