
# Zadanie 11: Generowanie prostego testu jednostkowego

## Cel zadania

Celem zadania jest wygenerowanie testu jednostkowego dla prostej funkcji JavaScript przy użyciu frameworka Jest oraz poznanie sposobu instalacji i uruchamiania testów.

## Funkcja JavaScript

```javascript
function sum(a, b) {
  return a + b;
}
```

## Prompt

Napisz prosty test jednostkowy dla tej funkcji używając Jest. Wyjaśnij, czym jest Jest, jak go zainstalować w projekcie i jak uruchomić ten test. Podaj również strukturę plików projektu.

## Odpowiedź ChatGPT

### Czym jest Jest?

Jest to framework do testowania kodu JavaScript. Umożliwia automatyczne sprawdzanie, czy funkcje działają zgodnie z oczekiwaniami.

Jest pozwala tworzyć testy jednostkowe, czyli testy sprawdzające pojedyncze funkcje lub fragmenty aplikacji.

### Struktura plików projektu

```text
projekt/
├── sum.js
├── sum.test.js
├── zadanie-11.md
├── package.json
└── node_modules/
```

- `sum.js` – plik zawierający funkcję dodawania.
- `sum.test.js` – plik z testami jednostkowymi.
- `zadanie-11.md` – dokumentacja zadania.
- `package.json` – konfiguracja projektu Node.js.
- `node_modules/` – zainstalowane zależności projektu.

### Kod funkcji – sum.js

```javascript
function sum(a, b) {
  return a + b;
}

module.exports = sum;
```

Funkcja przyjmuje dwa argumenty `a` i `b`, a następnie zwraca ich sumę. Instrukcja `module.exports` pozwala korzystać z funkcji w innych plikach.

### Kod testu – sum.test.js

```javascript
const sum = require('./sum');

test('dodaje 2 + 3 i zwraca 5', () => {
  expect(sum(2, 3)).toBe(5);
});

test('dodaje dwie liczby ujemne', () => {
  expect(sum(-2, -3)).toBe(-5);
});

test('dodaje zero do liczby', () => {
  expect(sum(5, 0)).toBe(5);
});
```

### Wyjaśnienie testu

- `require('./sum')` – importuje funkcję z pliku `sum.js`.
- `test()` – definiuje pojedynczy przypadek testowy.
- `expect()` – określa wynik, który chcemy sprawdzić.
- `toBe()` – porównuje otrzymany wynik z oczekiwaną wartością.

Pierwszy test sprawdza dodawanie dwóch liczb dodatnich, drugi dwóch liczb ujemnych, a trzeci dodawanie zera.

### Instalacja Jest

**1.** Otwórz terminal w folderze projektu.

**2.** Jeśli projekt nie ma jeszcze pliku `package.json`, wykonaj:

```bash
npm init -y
```

**3.** Zainstaluj Jest:

```bash
npm install --save-dev jest
```

**4.** W pliku `package.json` ustaw skrypt testowy:

```json
"scripts": {
  "test": "jest"
}
```

Jeśli sekcja `scripts` już istnieje, wystarczy zmienić lub dodać pole `test`.

### Uruchomienie testu

Aby uruchomić testy, wpisz w terminalu:

```bash
npm test
```

Jest automatycznie znajdzie plik `sum.test.js` i wykona zapisane w nim testy.

### Oczekiwany rezultat

Jeśli funkcja działa poprawnie, wszystkie trzy testy powinny zakończyć się powodzeniem.

Przykładowy wynik:

```text
PASS ./sum.test.js

Tests:       3 passed, 3 total
Test Suites: 1 passed, 1 total
```

## Wnioski i obserwacje

Jest umożliwia automatyczne sprawdzanie poprawności działania funkcji JavaScript. Dzięki testom jednostkowym można szybko wykrywać błędy po wprowadzeniu zmian w kodzie.

Wygenerowane testy sprawdzają funkcję `sum()` dla różnych wartości, co pozwala upewnić się, że poprawnie wykonuje podstawowe operacje dodawania.
