
# Zadanie 25: Generowanie prostego Jenkinsfile

## Cel zadania

Celem zadania jest wykorzystanie AI do wygenerowania deklaratywnego pipeline'u Jenkins dla aplikacji Node.js oraz poznanie działania jego poszczególnych etapów.

## Prompt 1

Wygeneruj prosty Jenkinsfile dla aplikacji Node.js, który będzie zawierał etapy:
- checkout kodu z repozytorium
- instalacja zależności (npm install)
- uruchomienie testów (npm test)
- budowanie aplikacji (npm run build)
- budowanie obrazu Docker
- publikowanie obrazu do rejestru Docker

Użyj składni deklaratywnej Jenkinsa.

## Wygenerowany Jenkinsfile

Kod pipeline'u został zapisany w pliku `Jenkinsfile`.

Pipeline wykorzystuje składnię deklaratywną Jenkinsa i składa się z sześciu etapów.

## Prompt 2

Wyjaśnij, co dokładnie dzieje się w każdym etapie tego Jenkinsfile i jakie są najlepsze praktyki przy tworzeniu pipeline'ów Jenkins.

## Wyjaśnienie działania Jenkinsfile

### 1. Agent

```groovy
agent any
```

Instrukcja `agent any` oznacza, że Jenkins może uruchomić pipeline na dowolnym dostępnym agencie.

Agent musi posiadać odpowiednie narzędzia, takie jak Node.js, npm i Docker.

W przedstawionym przykładzie używane jest polecenie `sh`, dlatego agent powinien działać na systemie Linux.

### 2. Zmienne środowiskowe

```groovy
environment {
    DOCKER_IMAGE = 'twoj-login/simple-node-app'
    DOCKER_CREDENTIALS = 'dockerhub-credentials'
}
```

Sekcja `environment` definiuje zmienne wykorzystywane w pipeline.

- `DOCKER_IMAGE` – nazwa obrazu Docker.
- `DOCKER_CREDENTIALS` – identyfikator danych logowania zapisanych w Jenkins.

### 3. Etap Checkout

```groovy
stage('Checkout') {
    steps {
        checkout scm
    }
}
```

Jenkins pobiera kod źródłowy aplikacji z repozytorium skonfigurowanego dla zadania.

Dzięki temu kolejne etapy pracują na aktualnej wersji kodu.

### 4. Etap Install Dependencies

```groovy
stage('Install Dependencies') {
    steps {
        sh 'npm install'
    }
}
```

Polecenie `npm install` instaluje zależności aplikacji zdefiniowane w pliku `package.json`.

Jest to niezbędne, aby aplikacja mogła zostać przetestowana i zbudowana.

### 5. Etap Test

```groovy
stage('Test') {
    steps {
        sh 'npm test'
    }
}
```

Jenkins uruchamia testy aplikacji.

Jeżeli polecenie zakończy się błędem, pipeline zostanie przerwany i nie przejdzie do kolejnych etapów.

Pozwala to uniknąć publikowania obrazu zawierającego kod, który nie przeszedł testów.

### 6. Etap Build Application

```groovy
stage('Build Application') {
    steps {
        sh 'npm run build'
    }
}
```

Jenkins uruchamia proces budowania aplikacji.

Polecenie wykonuje skrypt `build` zdefiniowany w pliku `package.json`.

W zależności od projektu może to oznaczać np. kompilację kodu lub przygotowanie plików produkcyjnych.

### 7. Etap Build Docker Image

```groovy
stage('Build Docker Image') {
    steps {
        sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .'
    }
}
```

Jenkins buduje obraz Docker na podstawie pliku `Dockerfile`.

Obraz otrzymuje nazwę określoną w zmiennej `DOCKER_IMAGE` oraz tag odpowiadający numerowi wykonania pipeline'u (`BUILD_NUMBER`).

Dzięki temu kolejne wersje obrazu można od siebie odróżnić.

### 8. Etap Push Docker Image

```groovy
stage('Push Docker Image') {
    steps {
        withCredentials([
            usernamePassword(
                credentialsId: "${DOCKER_CREDENTIALS}",
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )
        ]) {
            sh '''
                echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                docker push "$DOCKER_IMAGE:$BUILD_NUMBER"
                docker logout
            '''
        }
    }
}
```

W tym etapie Jenkins:

1. Pobiera dane logowania z Jenkins Credentials.
2. Loguje się do rejestru Docker.
3. Publikuje zbudowany obraz.
4. Wylogowuje się z rejestru.

Zastosowanie `withCredentials` pozwala uniknąć wpisywania hasła bezpośrednio w kodzie Jenkinsfile.

### 9. Sekcja Post

```groovy
post {
    success {
        echo 'Pipeline zakończony sukcesem!'
    }
    failure {
        echo 'Pipeline zakończony błędem!'
    }
}
```

Sekcja `post` określa działania wykonywane po zakończeniu pipeline'u.

W tym przypadku Jenkins wyświetla komunikat o powodzeniu lub niepowodzeniu.

## Najlepsze praktyki tworzenia pipeline'ów Jenkins

**1. Przechowywanie haseł w Jenkins Credentials**

Dane logowania i tokeny powinny być przechowywane w bezpiecznym magazynie danych, a nie bezpośrednio w Jenkinsfile.

**2. Automatyczne uruchamianie testów**

Testy powinny być wykonywane przed budowaniem i publikowaniem aplikacji, aby wykrywać błędy na wczesnym etapie.

**3. Podział pipeline'u na etapy**

Oddzielne etapy ułatwiają analizę działania pipeline'u i identyfikowanie miejsca wystąpienia błędu.

**4. Wersjonowanie obrazów Docker**

Warto stosować unikalne tagi obrazów, np. numer wykonania pipeline'u lub identyfikator commita.

Ułatwia to zarządzanie wersjami aplikacji.

**5. Korzystanie z npm ci**

W środowisku CI często lepiej używać `npm ci` zamiast `npm install`, ponieważ instaluje zależności zgodnie z plikiem `package-lock.json`.

W tym zadaniu wykorzystano jednak `npm install`, zgodnie z wymaganiami.

**6. Ograniczanie uprawnień**

Agent Jenkins powinien mieć tylko uprawnienia niezbędne do wykonywania pipeline'u. Dostęp do Dockera należy odpowiednio zabezpieczyć.

**7. Monitorowanie wyników**

Warto analizować logi wykonania pipeline'u oraz konfigurować powiadomienia o nieudanych uruchomieniach.

## Wymagania do uruchomienia

Aby pipeline działał poprawnie, potrzebne są:

- Jenkins z obsługą Pipeline.
- Agent Linux z Node.js, npm i Dockerem.
- Repozytorium Git z kodem aplikacji.
- Plik `package.json` ze skryptami `test` i `build`.
- Plik `Dockerfile`.
- Skonfigurowane dane logowania do rejestru Docker.

## Wnioski i obserwacje

AI wygenerowało deklaratywny Jenkinsfile zawierający wszystkie wymagane etapy: pobranie kodu, instalację zależności, testowanie, budowanie aplikacji, tworzenie obrazu Docker i jego publikację.

Podział na etapy sprawia, że pipeline jest czytelny i łatwiejszy w utrzymaniu.

Szczególnie ważne jest bezpieczne przechowywanie danych logowania oraz wykonywanie testów przed publikacją obrazu.

Zadanie pokazało, że AI może pomóc w szybkim przygotowaniu podstawowej konfiguracji CI/CD, jednak przed jej uruchomieniem należy dostosować ją do środowiska Jenkins i konkretnej aplikacji.
