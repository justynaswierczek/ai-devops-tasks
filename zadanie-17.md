
# Zadanie 17: Generowanie kodu na podstawie opisu

## Cel zadania

Celem zadania jest wygenerowanie funkcji JavaScript na podstawie opisu wymagań dotyczących filtrowania, sortowania i przekształcania danych.

## Opis funkcjonalności

Potrzebuję funkcji JavaScript, która:
- przyjmuje tablicę obiektów reprezentujących zadania (każdy z polami: id, title, status)
- filtruje tylko zadania o statusie "completed"
- sortuje je według id (rosnąco)
- zwraca tablicę zawierającą tylko tytuły tych zadań

## Prompt

Zaimplementuj funkcję JavaScript zgodnie z podanymi wymaganiami.

## Wygenerowana funkcja

Kod funkcji zapisano w pliku `task-filter.js`.

```javascript
function getCompletedTaskTitles(tasks) {
  return tasks
    .filter(task => task.status === 'completed')
    .sort((a, b) => a.id - b.id)
    .map(task => task.title);
}
```

## Wyjaśnienie działania funkcji

**1. `getCompletedTaskTitles(tasks)`**

Funkcja przyjmuje tablicę obiektów reprezentujących zadania. Każdy obiekt zawiera identyfikator `id`, tytuł `title` oraz status `status`.

**2. `filter()`**

```javascript
.filter(task => task.status === 'completed')
```

Metoda `filter()` wybiera tylko zadania, których status ma wartość `completed`. Pozostałe zadania są pomijane.

**3. `sort()`**

```javascript
.sort((a, b) => a.id - b.id)
```

Metoda `sort()` sortuje wybrane zadania rosnąco według pola `id`.

**4. `map()`**

```javascript
.map(task => task.title)
```

Metoda `map()` tworzy nową tablicę zawierającą wyłącznie tytuły zadań.

**5. `return`**

Instrukcja `return` zwraca końcową tablicę tytułów.

## Przykład użycia

```javascript
const tasks = [
  { id: 3, title: 'Napisać dokumentację', status: 'completed' },
  { id: 1, title: 'Przygotować projekt', status: 'completed' },
  { id: 4, title: 'Przetestować aplikację', status: 'pending' },
  { id: 2, title: 'Napisać kod', status: 'completed' }
];

console.log(getCompletedTaskTitles(tasks));
```

## Wynik działania

```text
[
  'Przygotować projekt',
  'Napisać kod',
  'Napisać dokumentację'
]
```

Zadanie o statusie `pending` zostało pominięte, ponieważ funkcja wybiera tylko zadania zakończone.

Pozostałe zadania zostały posortowane według identyfikatora `id` od najmniejszego do największego, a następnie zwrócono ich tytuły.

## Wnioski i obserwacje

AI wygenerowało funkcję zgodną z podanymi wymaganiami. Zastosowanie metod `filter()`, `sort()` i `map()` pozwoliło zapisać rozwiązanie w krótkiej i czytelnej formie.

Funkcja nie wymaga dodatkowych bibliotek i może być wykorzystana w aplikacjach JavaScript do przetwarzania list zadań.
