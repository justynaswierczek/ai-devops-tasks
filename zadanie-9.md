
# Zadanie 9: Weryfikacja prostego YAML

## Cel zadania

Celem zadania jest sprawdzenie poprawności pliku YAML wykorzystywanego w Docker Compose oraz poprawienie znalezionych błędów.

## Prompt 1

Sprawdź, czy poniższy plik YAML jest poprawny. Jeśli zawiera błędy, wskaż je i wyjaśnij.

## Oryginalny plik YAML

```yaml
services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    build: .
    ports
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD=password
```

## Znalezione błędy

**1. Brak dwukropka po `ports`**

W konfiguracji usługi `app` zapisano:

```yaml
ports
  - "3000:3000"
```

Brakuje dwukropka po słowie `ports`. Powoduje to błąd składni YAML.

Poprawny zapis:

```yaml
ports:
  - "3000:3000"
```

**2. Nieprawidłowy zapis zmiennej środowiskowej**

W usłudze `db` zapisano:

```yaml
environment:
  POSTGRES_PASSWORD=password
```

Taki zapis nie jest prawidłową mapą zmiennych środowiskowych w Docker Compose. Należy użyć dwukropka lub zapisu listowego.

Poprawny zapis:

```yaml
environment:
  POSTGRES_PASSWORD: password
```

**3. Dodatkowe uwagi**

Pozostała struktura pliku jest poprawna. Usługi `web`, `app` i `db` zostały prawidłowo zdefiniowane.

W praktycznym projekcie hasło do bazy danych powinno być przechowywane bezpieczniej, np. w zmiennej środowiskowej, zamiast wpisywania go bezpośrednio do pliku.

## Prompt 2

Popraw znalezione błędy w pliku YAML i przedstaw jego prawidłową wersję.

## Poprawiona wersja YAML

```yaml
services:
  web:
    image: nginx
    ports:
      - "80:80"

  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db

  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: password
```

## Wyjaśnienie poprawek

W poprawionej wersji dodano brakujący dwukropek po `ports` w usłudze `app` oraz zmieniono zapis zmiennej środowiskowej `POSTGRES_PASSWORD` na prawidłową składnię YAML.

Zachowano oryginalną strukturę trzech usług:
- `web` – serwer Nginx działający na porcie 80.
- `app` – aplikacja budowana z lokalnego Dockerfile, udostępniana na porcie 3000.
- `db` – baza danych PostgreSQL.

## Wnioski i obserwacje

AI wykryło błędy w konfiguracji YAML i zaproponowało ich poprawienie. Najważniejszym problemem był brak dwukropka po `ports`, który uniemożliwiał prawidłowe odczytanie pliku.

Zadanie pokazało, że AI może być pomocne przy sprawdzaniu składni plików konfiguracyjnych i wyjaśnianiu błędów w prosty sposób.
