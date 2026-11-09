
# Zadanie 12: Optymalizacja prostego skryptu

## Cel zadania

Celem zadania jest analiza funkcji Python wyszukującej duplikaty na liście oraz zaproponowanie bardziej wydajnego rozwiązania.

## Oryginalny kod Python

```python
def find_duplicates(list_of_items):
    duplicates = []
    for i in range(len(list_of_items)):
        for j in range(i+1, len(list_of_items)):
            if list_of_items[i] == list_of_items[j] and list_of_items[i] not in duplicates:
                duplicates.append(list_of_items[i])
    return duplicates
```

## Prompt

Czy ten kod można zoptymalizować? Jeśli tak, zaproponuj bardziej wydajną wersję.

## Odpowiedź ChatGPT

Tak, kod można zoptymalizować. Oryginalna funkcja wykorzystuje dwie zagnieżdżone pętle, które porównują elementy listy między sobą. Przy dużej liczbie elementów może to powodować długi czas wykonywania.

Lepszym rozwiązaniem jest wykorzystanie zbiorów (`set`), które pozwalają szybko sprawdzać, czy dany element wystąpił już wcześniej.

## Zoptymalizowany kod Python

```python
def find_duplicates(list_of_items):
    seen = set()
    duplicates = set()
    result = []

    for item in list_of_items:
        if item in seen and item not in duplicates:
            duplicates.add(item)
            result.append(item)
        else:
            seen.add(item)

    return result
```

## Wyjaśnienie usprawnień

**1. Usunięcie zagnieżdżonych pętli**

W oryginalnym kodzie każdy element jest porównywany z kolejnymi elementami listy. W nowej wersji wystarczy jedna pętla `for`, która przechodzi przez wszystkie elementy.

**2. Wykorzystanie zbioru `seen`**

Zbiór `seen` przechowuje elementy, które zostały już napotkane. Dzięki temu można szybko sprawdzić, czy dany element wystąpił wcześniej.

**3. Wykorzystanie zbioru `duplicates`**

Zbiór `duplicates` przechowuje znalezione duplikaty. Zapobiega to wielokrotnemu dodawaniu tego samego elementu do wyniku.

**4. Zachowanie wyników w liście `result`**

Lista `result` przechowuje znalezione duplikaty w kolejności ich drugiego wystąpienia.

**5. Zmniejszenie złożoności czasowej**

Oryginalna funkcja ma złożoność czasową co najmniej O(n²), ponieważ wykorzystuje dwie zagnieżdżone pętle.

Zoptymalizowana wersja ma średnią złożoność czasową O(n), ponieważ przechodzi przez listę tylko raz, a operacje na zbiorach są zazwyczaj wykonywane w czasie O(1).

## Przykład działania

Dane wejściowe:

```python
items = [1, 2, 3, 2, 4, 1, 5, 3]
print(find_duplicates(items))
```

Wynik zoptymalizowanej funkcji:

```text
[2, 1, 3]
```

Funkcja zwraca elementy, które występują na liście więcej niż jeden raz.

## Porównanie wersji

| Cecha | Oryginalny kod | Zoptymalizowany kod |
|---|---|---|
| Liczba pętli | Dwie zagnieżdżone | Jedna |
| Złożoność czasowa | O(n²) lub większa | Średnio O(n) |
| Wyszukiwanie duplikatów | Porównywanie elementów | Zbiory `set` |
| Wydajność dla dużych list | Niższa | Wyższa |
| Dodatkowa pamięć | Lista duplikatów | Dwa zbiory i lista |

## Wnioski i obserwacje

Zoptymalizowana funkcja jest bardziej wydajna, ponieważ eliminuje konieczność wielokrotnego porównywania tych samych elementów.

Wykorzystanie zbiorów `set` pozwala znacznie przyspieszyć wyszukiwanie duplikatów, szczególnie w przypadku dużych list.

Wadą nowego rozwiązania jest dodatkowe zużycie pamięci oraz konieczność korzystania z elementów, które można przechowywać w zbiorach, czyli obiektów hashowalnych.

AI pomogło wskazać mniej wydajne fragmenty kodu i zaproponowało prostsze rozwiązanie.
