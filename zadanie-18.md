
# Zadanie 18: Analiza wymagań bezpieczeństwa

## Cel zadania

Celem zadania jest poznanie podstawowych praktyk bezpieczeństwa aplikacji Dockerowych w środowisku produkcyjnym oraz przedstawienie przykładu implementacji jednej z nich.

## Prompt 1

Jakie są 5 kluczowych praktyk bezpieczeństwa dla aplikacji Dockerowych w środowisku produkcyjnym?

## Odpowiedź ChatGPT

### 1. Uruchamianie kontenerów bez uprawnień root

Domyślnie procesy w kontenerze mogą działać jako użytkownik root. W środowisku produkcyjnym zaleca się uruchamianie aplikacji jako użytkownik z ograniczonymi uprawnieniami.

Zmniejsza to ryzyko związane z przejęciem aplikacji przez osobę nieuprawnioną.

### 2. Korzystanie z aktualnych i zaufanych obrazów

Należy wykorzystywać obrazy pochodzące z zaufanych źródeł oraz regularnie aktualizować ich wersje.

Warto również skanować obrazy pod kątem znanych podatności za pomocą narzędzi takich jak Trivy.

### 3. Ograniczanie uprawnień i zasobów kontenerów

Kontenery powinny mieć dostęp tylko do niezbędnych zasobów systemowych.

Można stosować ograniczenia pamięci i procesora, usuwać zbędne uprawnienia systemowe oraz korzystać z systemu plików w trybie tylko do odczytu.

### 4. Bezpieczne przechowywanie danych poufnych

Hasła, tokeny i klucze API nie powinny być zapisywane bezpośrednio w Dockerfile ani umieszczane w obrazach kontenerów.

Do przechowywania poufnych informacji można wykorzystać mechanizmy zarządzania sekretami lub zewnętrzne narzędzia przeznaczone do tego celu.

### 5. Ograniczanie dostępu sieciowego

Należy udostępniać tylko porty wymagane do działania aplikacji oraz ograniczać komunikację między kontenerami.

Pomocne jest stosowanie oddzielnych sieci Docker i odpowiedniej konfiguracji zapory sieciowej.

## Prompt 2

Jak mogę zaimplementować pierwszą z tych praktyk w moim Dockerfile i docker-compose.yml?

## Odpowiedź ChatGPT

Pierwszą praktyką jest uruchamianie kontenera bez uprawnień użytkownika root.

Można ją wdrożyć poprzez utworzenie użytkownika z ograniczonymi uprawnieniami w Dockerfile oraz ustawienie odpowiedniego użytkownika w konfiguracji Docker Compose.

### Przykład Dockerfile

Poniższy przykład dotyczy prostej aplikacji Node.js.

```dockerfile
FROM node:22-alpine

WORKDIR /app

COPY --chown=node:node package*.json ./

RUN npm ci --omit=dev

COPY --chown=node:node . .

USER node

EXPOSE 3000

CMD ["node", "server.js"]
```

### Wyjaśnienie Dockerfile

1. `FROM node:22-alpine` – wykorzystuje obraz Node.js oparty na Alpine Linux.
2. `WORKDIR /app` – ustawia katalog roboczy aplikacji.
3. `COPY --chown=node:node` – kopiuje pliki i przypisuje je do użytkownika `node`.
4. `RUN npm ci --omit=dev` – instaluje zależności produkcyjne aplikacji.
5. `USER node` – uruchamia kolejne instrukcje i proces aplikacji jako użytkownik bez uprawnień root.
6. `EXPOSE 3000` – dokumentuje port wykorzystywany przez aplikację.
7. `CMD ["node", "server.js"]` – uruchamia aplikację.

Najważniejsza jest instrukcja `USER node`, która ogranicza uprawnienia procesu działającego w kontenerze.

### Przykład docker-compose.yml

```yaml
services:
  app:
    build: .
    user: "node"
    ports:
      - "3000:3000"
    security_opt:
      - no-new-privileges:true
```

### Wyjaśnienie docker-compose.yml

- `build: .` – buduje obraz na podstawie lokalnego Dockerfile.
- `user: "node"` – określa użytkownika, z którego uprawnieniami będzie uruchamiany proces.
- `ports` – udostępnia aplikację na porcie 3000.
- `security_opt` – opcja `no-new-privileges:true` zapobiega uzyskiwaniu dodatkowych uprawnień przez procesy w kontenerze.

W tym przykładzie aplikacja nie jest uruchamiana jako root, co ogranicza potencjalne skutki naruszenia bezpieczeństwa.

### Sprawdzenie konfiguracji

Po uruchomieniu kontenera można sprawdzić użytkownika za pomocą polecenia:

```bash
docker compose exec app whoami
```

Oczekiwany wynik:

```text
node
```

Oznacza to, że polecenie zostało wykonane jako użytkownik `node`, a nie `root`.

## Podsumowanie

Bezpieczeństwo aplikacji Dockerowych wymaga stosowania kilku praktyk jednocześnie, takich jak ograniczanie uprawnień, aktualizowanie obrazów, ochrona danych poufnych i kontrolowanie dostępu sieciowego.

Uruchamianie kontenerów bez uprawnień root jest jedną z podstawowych metod ograniczania ryzyka. Można ją wdrożyć za pomocą instrukcji `USER` w Dockerfile oraz ustawienia `user` w Docker Compose.

## Wnioski i obserwacje

AI przedstawiło pięć podstawowych praktyk bezpieczeństwa Dockera, a następnie pokazało sposób wdrożenia jednej z nich na konkretnym przykładzie.

Dzięki pytaniu uzupełniającemu odpowiedź stała się bardziej praktyczna i zawierała gotowe fragmenty konfiguracji.

Zadanie pokazało, że AI może pomóc nie tylko w poznaniu zasad bezpieczeństwa, ale również w ich zastosowaniu podczas konfiguracji kontenerów.
