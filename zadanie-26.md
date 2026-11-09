
# Zadanie 26: Analiza i poprawa istniejącego Jenkinsfile

## Cel zadania

Celem zadania jest wykorzystanie AI do znalezienia błędów w konfiguracji Jenkins Pipeline, poprawienia ich oraz wyjaśnienia wprowadzonych zmian.

## Prompt

Ten Jenkinsfile zawiera kilka błędów. Znajdź je i zaproponuj poprawioną wersję. Wyjaśnij, jakie były problemy i jak je naprawiłeś.

## Oryginalny Jenkinsfile

Oryginalny kod z błędami zapisano w pliku `Jenkinsfile-with-errors`.

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            stesp {
                sh 'npm install'
                sh 'npm build'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker build -t myapp .'
                sh 'docker push myapp:latest'
            }
            when {
                branch 'master'
            }
        }
    }
}
```

## Znalezione błędy i problemy

### 1. Literówka w instrukcji steps

**Błędny kod:**

```groovy
stesp {
    sh 'npm install'
    sh 'npm build'
}
```

**Poprawny kod:**

```groovy
steps {
    sh 'npm install'
    sh 'npm run build'
}
```

W oryginalnym Jenkinsfile zapisano `stesp` zamiast `steps`.

Jest to błąd składni deklaratywnego pipeline'u, który uniemożliwia prawidłowe wykonanie konfiguracji.

### 2. Nieprawidłowe polecenie budowania aplikacji

**Błędny kod:**

```groovy
sh 'npm build'
```

**Poprawny kod:**

```groovy
sh 'npm run build'
```

Polecenie `npm build` nie służy do standardowego uruchamiania skryptu `build` z pliku `package.json`.

Poprawna forma to `npm run build`.

### 3. Niespójne oznaczanie obrazu Docker

**Błędny kod:**

```groovy
sh 'docker build -t myapp .'
sh 'docker push myapp:latest'
```

**Poprawny kod:**

```groovy
sh 'docker build -t $DOCKER_IMAGE:$BUILD_NUMBER .'
sh 'docker push $DOCKER_IMAGE:$BUILD_NUMBER'
```

W oryginalnej wersji obraz był budowany lokalnie pod nazwą `myapp`, a następnie publikowany z tagiem `latest`.

Samo oznaczenie `myapp` podczas budowania domyślnie nadaje tag `latest`, więc nie jest to bezpośredni błąd zgodności tagów.

Problem polega jednak na braku nazwy konta lub przestrzeni nazw rejestru oraz stosowaniu jednego tagu dla kolejnych wersji.

W poprawionej wersji użyto zmiennej `DOCKER_IMAGE` oraz numeru wykonania pipeline'u `BUILD_NUMBER`.

### 4. Brak logowania do rejestru Docker

W oryginalnej wersji nie uwzględniono uwierzytelniania przed publikacją obrazu.

Dodano:

```groovy
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
```

Dane logowania są pobierane z Jenkins Credentials zamiast być zapisane bezpośrednio w kodzie.

Pozwala to bezpieczniej publikować obrazy Docker.

### 5. Warunek uruchomienia etapu Deploy

Oryginalny kod zawierał:

```groovy
when {
    branch 'master'
}
```

Sam warunek jest poprawny składniowo i nie wymaga zmiany.

Przeniesiono go przed sekcję `steps`, aby konfiguracja była bardziej czytelna.

Warunek sprawia, że etap Deploy jest wykonywany tylko dla gałęzi `master`, jeżeli Jenkins udostępnia informacje o gałęzi, np. w Multibranch Pipeline.

### 6. Brak komunikatów o wyniku pipeline'u

W oryginalnym Jenkinsfile nie było sekcji `post`.

Dodano:

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

Dzięki temu Jenkins wyświetla odpowiedni komunikat po zakończeniu pipeline'u.

Jest to dodatkowe usprawnienie, a nie poprawka błędu składniowego.

## Podsumowanie zmian

| Problem | Wprowadzona poprawka |
|---|---|
| Literówka `stesp` | Zmiana na `steps` |
| Polecenie `npm build` | Zmiana na `npm run build` |
| Mało precyzyjne tagowanie obrazu | Użycie nazwy obrazu i `BUILD_NUMBER` |
| Brak logowania do rejestru | Dodanie `withCredentials` |
| Czytelność warunku Deploy | Umieszczenie `when` przed `steps` |
| Brak komunikatów końcowych | Dodanie sekcji `post` |

## Poprawiony Jenkinsfile

Poprawioną konfigurację zapisano w pliku `Jenkinsfile-fixed`.

Pipeline zawiera trzy główne etapy:

1. **Build** – instalacja zależności i budowanie aplikacji Node.js.
2. **Test** – uruchomienie testów aplikacji.
3. **Deploy** – budowanie obrazu Docker i publikacja do rejestru, tylko dla gałęzi `master`.

## Wnioski i obserwacje

AI pomogło wykryć błędy w Jenkinsfile oraz zaproponowało poprawioną wersję konfiguracji.

Najważniejsze problemy dotyczyły literówki w instrukcji `steps` oraz nieprawidłowego polecenia budowania aplikacji.

Dodatkowo poprawiono sposób publikowania obrazu Docker, uwzględniono bezpieczne pobieranie danych logowania oraz dodano komunikaty o wyniku pipeline'u.

Zadanie pokazało, że AI może pomóc zarówno w wykrywaniu błędów składniowych, jak i we wskazywaniu dobrych praktyk podczas tworzenia pipeline'ów CI/CD.
