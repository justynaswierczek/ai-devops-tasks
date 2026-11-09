
# Zadanie 15: Refaktoryzacja prostej funkcji

## Cel zadania

Celem zadania jest refaktoryzacja funkcji JavaScript, która zwraca konfigurację aplikacji w zależności od środowiska. Refaktoryzacja ma poprawić czytelność kodu i ułatwić jego utrzymanie bez zmiany dotychczasowego działania.

## Prompt

Zrefaktoryzuj tę funkcję, aby była bardziej czytelna i łatwiejsza w utrzymaniu.

## Oryginalna funkcja

Oryginalną funkcję zapisano w pliku `config.js`.

Funkcja `getEnvironmentConfig(env)` wykorzystuje instrukcje `if-else`, aby zwrócić odpowiednią konfigurację dla jednego z czterech środowisk:

- `development` – środowisko programistyczne.
- `testing` – środowisko testowe.
- `staging` – środowisko przedprodukcyjne.
- `production` – środowisko produkcyjne.

Jeżeli podano nieznane środowisko, funkcja zwraca konfigurację `development`.

## Zrefaktoryzowana funkcja

Zrefaktoryzowaną wersję zapisano w pliku `config-refactored.js`.

```javascript
const configs = {
  development: {
    apiUrl: 'http://localhost:3000/api',
    debug: true,
    timeout: 5000
  },
  testing: {
    apiUrl: 'http://test-server:3000/api',
    debug: true,
    timeout: 5000
  },
  staging: {
    apiUrl: 'https://staging.example.com/api',
    debug: false,
    timeout: 10000
  },
  production: {
    apiUrl: 'https://api.example.com',
    debug: false,
    timeout: 15000
  }
};

function getEnvironmentConfig(env) {
  return Object.hasOwn(configs, env)
    ? configs[env]
    : configs.development;
}
```

## Opis wprowadzonych zmian

**1. Usunięcie wielu instrukcji if-else**

W oryginalnej funkcji każde środowisko było sprawdzane za pomocą osobnego warunku. W nowej wersji zastąpiono je jednym obiektem `configs`.

**2. Oddzielenie danych od logiki**

Wszystkie konfiguracje zostały umieszczone w jednym obiekcie, a funkcja odpowiada jedynie za wybór odpowiedniej konfiguracji.

**3. Uproszczenie funkcji**

Zamiast wielu warunków funkcja wykorzystuje dostęp do właściwości obiektu na podstawie wartości parametru `env`.

**4. Zachowanie konfiguracji domyślnej**

Jeżeli podane środowisko nie istnieje w obiekcie, funkcja zwraca konfigurację `development`, tak samo jak w oryginalnej wersji.

## Korzyści z refaktoryzacji

- **Większa czytelność** – kod jest krótszy i bardziej przejrzysty.
- **Łatwiejsze utrzymanie** – wszystkie konfiguracje znajdują się w jednym miejscu.
- **Prostsza rozbudowa** – dodanie nowego środowiska wymaga jedynie dopisania kolejnego wpisu do obiektu.
- **Mniej powtarzającego się kodu** – nie trzeba tworzyć kolejnych instrukcji `else if`.
- **Zachowanie funkcjonalności** – funkcja nadal zwraca te same ustawienia dla poszczególnych środowisk.

## Przykład działania

```javascript
console.log(getEnvironmentConfig('production'));
```

Oczekiwany wynik:

```javascript
{
  apiUrl: 'https://api.example.com',
  debug: false,
  timeout: 15000
}
```

Dla nieznanego środowiska, np. `unknown`, funkcja zwróci konfigurację `development`.

## Wnioski i obserwacje

Refaktoryzacja pozwoliła uprościć funkcję bez zmiany jej podstawowego działania. Zastosowanie obiektu konfiguracyjnego zamiast wielu instrukcji warunkowych sprawia, że kod jest bardziej czytelny i łatwiejszy do rozbudowy.

AI pomogło wskazać sposób ograniczenia powtarzającego się kodu i zaproponowało rozwiązanie, które będzie wygodniejsze w utrzymaniu.
