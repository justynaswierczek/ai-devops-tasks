
# Zadanie 20: Generowanie wyrażeń regularnych

## Cel zadania

Celem zadania jest wykorzystanie AI do wygenerowania wyrażenia regularnego (regex), które sprawdza poprawność formatu adresu IPv4, oraz zaimplementowanie go w JavaScript.

## Prompt 1

Potrzebuję wyrażenia regularnego, które waliduje format adresu IPv4 (np. 192.168.1.1).

## Wygenerowane wyrażenie regularne

```regex
^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$
```

Wyrażenie sprawdza, czy adres składa się z czterech liczb oddzielonych kropkami, a każda liczba mieści się w zakresie od 0 do 255.

## Prompt 2

Wyjaśnij, jak działa to wyrażenie regularne i przetestuj je na kilku przykładach (poprawnych i niepoprawnych).

## Wyjaśnienie działania regex

**1. `^`**

Oznacza początek tekstu. Dzięki temu przed adresem IP nie mogą występować dodatkowe znaki.

**2. `25[0-5]`**

Dopasowuje liczby od 250 do 255.

**3. `2[0-4]\d`**

Dopasowuje liczby od 200 do 249.

**4. `1\d{2}`**

Dopasowuje liczby od 100 do 199.

**5. `[1-9]?\d`**

Dopasowuje liczby od 0 do 99, bez zer wiodących, np. `1`, `9`, `25`, `99`.

**6. `\.`**

Oznacza dosłowną kropkę oddzielającą części adresu IPv4.

**7. `{3}`**

Oznacza, że fragment zawierający kropkę i kolejną liczbę musi wystąpić dokładnie trzy razy.

W połączeniu z pierwszą liczbą daje to cztery części adresu IPv4.

**8. `$`**

Oznacza koniec tekstu. Dzięki temu po adresie IP nie mogą występować dodatkowe znaki.

## Implementacja w JavaScript

Funkcja została zapisana w pliku `ipv4-validator.js`.

```javascript
function isValidIPv4(ip) {
  const regex = /^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$/;

  return regex.test(ip);
}
```

Metoda `test()` sprawdza, czy podany tekst pasuje do wyrażenia regularnego.

Jeżeli adres jest poprawny, funkcja zwraca `true`. W przeciwnym przypadku zwraca `false`.

## Przykłady testów

| Adres IP | Oczekiwany wynik | Wyjaśnienie |
|---|---|---|
| `192.168.1.1` | `true` | Poprawny adres IPv4 |
| `8.8.8.8` | `true` | Poprawny adres IPv4 |
| `255.255.255.255` | `true` | Wszystkie liczby mieszczą się w zakresie |
| `0.0.0.0` | `true` | Poprawny format IPv4 |
| `256.100.50.25` | `false` | Liczba 256 przekracza 255 |
| `192.168.1` | `false` | Brakuje czwartej części adresu |
| `192.168.1.999` | `false` | Liczba 999 przekracza 255 |
| `192.168.01.1` | `false` | Niedozwolone zero wiodące |
| `abc.def.ghi.jkl` | `false` | Adres zawiera litery |

## Przykładowy kod testujący

```javascript
const addresses = [
  '192.168.1.1',
  '8.8.8.8',
  '255.255.255.255',
  '0.0.0.0',
  '256.100.50.25',
  '192.168.1',
  '192.168.1.999',
  '192.168.01.1',
  'abc.def.ghi.jkl'
];

addresses.forEach(ip => {
  console.log(`${ip}: ${isValidIPv4(ip)}`);
});
```

## Oczekiwany wynik

```text
192.168.1.1: true
8.8.8.8: true
255.255.255.255: true
0.0.0.0: true
256.100.50.25: false
192.168.1: false
192.168.1.999: false
192.168.01.1: false
abc.def.ghi.jkl: false
```

## Wnioski i obserwacje

AI pomogło wygenerować wyrażenie regularne do sprawdzania formatu adresów IPv4 oraz wyjaśniło znaczenie jego poszczególnych elementów.

Regex pozwala sprawdzić nie tylko obecność czterech liczb oddzielonych kropkami, ale również zakres wartości od 0 do 255.

Przykłady pokazują, że wyrażenie odrzuca adresy z nieprawidłowymi wartościami, brakującymi częściami oraz niedozwolonymi znakami.

Zastosowanie regex pozwala wykonać taką walidację bez konieczności tworzenia wielu instrukcji warunkowych.
