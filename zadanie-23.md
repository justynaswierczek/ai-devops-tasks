
# Zadanie 23: Analiza złożoności algorytmu

## Cel zadania

Celem zadania jest przeanalizowanie złożoności czasowej i pamięciowej algorytmu wyszukującego pary liczb o określonej sumie oraz przygotowanie jego zoptymalizowanej wersji.

## Prompt

Jaka jest złożoność czasowa i pamięciowa tego algorytmu? Czy można go zoptymalizować?

## Oryginalny algorytm

Oryginalny kod zapisano w pliku `find-pairs.js`.

```javascript
function findPairs(arr, targetSum) {
  const pairs = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] === targetSum) {
        pairs.push([arr[i], arr[j]]);
      }
    }
  }
  return pairs;
}
```

## Analiza złożoności oryginalnego algorytmu

### Złożoność czasowa – O(n²)

Algorytm wykorzystuje dwie zagnieżdżone pętle `for`.

Pierwsza pętla przechodzi przez wszystkie elementy tablicy, natomiast druga sprawdza kolejne elementy w poszukiwaniu pary o określonej sumie.

Liczba porównań wynosi:

`n * (n - 1) / 2`

Oznacza to, że liczba operacji rośnie kwadratowo wraz z liczbą elementów tablicy.

Dlatego złożoność czasowa wynosi **O(n²)**.

### Złożoność pamięciowa – O(k)

Algorytm zapisuje znalezione pary w tablicy `pairs`.

Jeżeli znaleziono `k` par, potrzeba pamięci proporcjonalnej do ich liczby.

W najgorszym przypadku liczba par może wynosić O(n²), dlatego całkowita złożoność pamięciowa w najgorszym przypadku wynosi **O(n²)**.

Nie licząc tablicy wynikowej, algorytm wykorzystuje tylko stałą ilość dodatkowej pamięci, czyli **O(1)**.

## Optymalizacja algorytmu

Zoptymalizowaną wersję zapisano w pliku `find-pairs-optimized.js`.

Zamiast dwóch zagnieżdżonych pętli wykorzystano strukturę danych `Map`, która przechowuje wcześniej napotkane liczby oraz liczbę ich wystąpień.

```javascript
function findPairs(arr, targetSum) {
  const pairs = [];
  const seen = new Map();

  for (const num of arr) {
    const complement = targetSum - num;
    const count = seen.get(complement) || 0;

    for (let i = 0; i < count; i++) {
      pairs.push([complement, num]);
    }

    seen.set(num, (seen.get(num) || 0) + 1);
  }

  return pairs;
}
```

## Wyjaśnienie działania zoptymalizowanej wersji

**1. Utworzenie struktury Map**

`const seen = new Map();`

Przechowuje liczby, które pojawiły się wcześniej, oraz liczbę ich wystąpień.

**2. Przejście przez tablicę**

`for (const num of arr)`

Algorytm przechodzi przez kolejne elementy tablicy.

**3. Obliczenie brakującej liczby**

`const complement = targetSum - num;`

Oblicza, jaka liczba jest potrzebna, aby suma dwóch elementów była równa `targetSum`.

**4. Wyszukanie pasujących elementów**

`seen.get(complement)`

Sprawdza, ile razy brakująca liczba pojawiła się wcześniej. Dla każdego wystąpienia dodawana jest odpowiednia para.

**5. Zapisanie aktualnej liczby**

`seen.set(num, (seen.get(num) || 0) + 1);`

Aktualizuje liczbę wystąpień danego elementu.

## Analiza złożoności zoptymalizowanego algorytmu

### Złożoność czasowa – O(n + k)

Przejście przez tablicę wymaga O(n) operacji.

Operacje wyszukiwania i zapisu w `Map` mają średnio złożoność O(1).

Dodatkowo algorytm musi zapisać wszystkie znalezione pary, których liczba wynosi `k`.

Dlatego średnia złożoność czasowa wynosi **O(n + k)**.

Jeżeli liczba par jest niewielka, działanie algorytmu jest zbliżone do O(n).

W najgorszym przypadku, gdy liczba par wynosi O(n²), całkowita złożoność nadal wynosi O(n²).

### Złożoność pamięciowa – O(n + k)

Struktura `Map` może przechowywać do `n` różnych liczb, dlatego wymaga O(n) dodatkowej pamięci.

Tablica wynikowa zajmuje O(k) pamięci.

Łączna złożoność pamięciowa wynosi **O(n + k)**.

## Porównanie algorytmów

| Cecha | Oryginalny algorytm | Zoptymalizowany algorytm |
|---|---|---|
| Metoda | Dwie pętle for | Map i jedna główna pętla |
| Czas | O(n²) | Średnio O(n + k) |
| Pamięć dodatkowa bez wyników | O(1) | O(n) |
| Pamięć z wynikami | O(k) | O(n + k) |
| Wyszukiwanie par | Porównywanie wszystkich par | Wyszukiwanie brakującej wartości |

`n` oznacza liczbę elementów wejściowych, a `k` liczbę znalezionych par.

## Przykład użycia

```javascript
const numbers = [2, 4, 3, 5, 7, 8];
const targetSum = 10;

console.log(findPairs(numbers, targetSum));
```

Oczekiwany wynik zoptymalizowanej wersji:

```text
[ [ 3, 7 ], [ 2, 8 ] ]
```

## Wnioski i obserwacje

Oryginalny algorytm ma złożoność czasową O(n²), ponieważ sprawdza wszystkie możliwe pary elementów.

Zastosowanie struktury `Map` pozwala ograniczyć liczbę niepotrzebnych porównań i przyspieszyć wyszukiwanie par, szczególnie gdy liczba znalezionych wyników jest niewielka.

Optymalizacja wymaga jednak dodatkowej pamięci do przechowywania wcześniej napotkanych wartości.

AI pomogło przeanalizować wydajność algorytmu oraz zaproponować rozwiązanie, które w typowych przypadkach może działać szybciej.
