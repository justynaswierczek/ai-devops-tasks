
# Zadanie 21: Transformacja danych

## Cel zadania

Celem zadania jest wykorzystanie AI do przekształcenia danych z formatu JSON do formatu CSV oraz zrozumienie różnic między tymi formatami.

## Prompt

Przekształć te dane JSON do formatu CSV z kolumnami: id, name, email, roles.

## Dane wejściowe – JSON

Oryginalne dane zapisano w pliku `users.json`.

```json
{
  "users": [
    {
      "id": 1,
      "name": "Jan Kowalski",
      "email": "jan@example.com",
      "roles": ["admin", "user"]
    },
    {
      "id": 2,
      "name": "Anna Nowak",
      "email": "anna@example.com",
      "roles": ["user"]
    }
  ]
}
```

## Dane wyjściowe – CSV

Wygenerowane dane zapisano w pliku `users.csv`.

```csv
id,name,email,roles
1,Jan Kowalski,jan@example.com,"admin;user"
2,Anna Nowak,anna@example.com,user
```

## Opis procesu konwersji

**1. Odczyt danych JSON**

Dane wejściowe zawierają tablicę `users`, w której znajdują się dwa obiekty reprezentujące użytkowników.

Każdy użytkownik posiada cztery pola: `id`, `name`, `email` oraz `roles`.

**2. Utworzenie kolumn CSV**

Na podstawie pól obiektów JSON utworzono cztery kolumny:

- `id` – identyfikator użytkownika.
- `name` – imię i nazwisko.
- `email` – adres e-mail.
- `roles` – role przypisane do użytkownika.

**3. Przekształcenie obiektów na wiersze**

Każdy obiekt użytkownika został przekształcony w jeden wiersz pliku CSV.

**4. Konwersja tablicy roles**

W JSON pole `roles` jest tablicą, która może zawierać kilka wartości.

CSV nie obsługuje bezpośrednio tablic, dlatego role zostały połączone w jeden tekst, a poszczególne wartości oddzielono średnikiem.

Przykład:

```json
"roles": ["admin", "user"]
```

Po konwersji:

```csv
"admin;user"
```

## Potencjalne wyzwania podczas konwersji

**1. Reprezentacja tablic**

Największym wyzwaniem jest zapisanie tablicy `roles` w pojedynczej komórce CSV. Zastosowano separator `;`, który pozwala zachować wszystkie role użytkownika.

**2. Utrata struktury danych**

JSON obsługuje zagnieżdżone obiekty i tablice, natomiast CSV przechowuje dane w postaci płaskiej tabeli. Przy bardziej złożonych danych może to prowadzić do utraty informacji o ich strukturze.

**3. Znaki specjalne**

Jeżeli wartości zawierają przecinki, cudzysłowy lub znaki nowej linii, należy je odpowiednio zapisać zgodnie z zasadami formatu CSV.

**4. Typy danych**

JSON rozróżnia m.in. liczby, tekst i wartości logiczne. W CSV wartości są zapisywane jako tekst, dlatego podczas ponownego importu może być konieczne określenie ich typów.

**5. Odtworzenie oryginalnych danych**

Aby ponownie przekształcić CSV na JSON, trzeba wiedzieć, że wartości w kolumnie `roles` są rozdzielone średnikiem. Należy również uwzględnić możliwość wystąpienia średnika w samej nazwie roli.

## Wnioski i obserwacje

AI poprawnie przekształciło dane JSON do formatu CSV, zachowując wszystkie wymagane kolumny i informacje o użytkownikach.

Najważniejszym elementem konwersji było odpowiednie zapisanie tablicy `roles`, ponieważ CSV nie obsługuje bezpośrednio złożonych struktur danych.

Zadanie pokazało, że AI może ułatwić transformację danych między formatami, jednak przy bardziej złożonych strukturach należy świadomie wybrać sposób reprezentacji informacji.
