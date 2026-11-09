
# Zadanie 29: Generowanie szablonu konfiguracji Jenkins

## Cel zadania

Celem zadania jest wykorzystanie AI do wygenerowania szablonu Jenkins Configuration as Code (JCasC), który umożliwia automatyczną konfigurację serwera Jenkins za pomocą pliku YAML.

## Prompt 1

Wygeneruj szablon Jenkins Configuration as Code (JCasC) w formacie YAML, który konfiguruje:
- podstawowe ustawienia Jenkins (liczba wykonawców, timeout)
- globalny katalog narzędzi (Maven, Node.js, Docker)
- podstawowe wtyczki
- przykładowe zadanie typu pipeline

## Wygenerowana konfiguracja

Szablon zapisano w pliku `jenkins-casc.yaml`.

Konfiguracja obejmuje:
- Ustawienie dwóch wykonawców Jenkins.
- Zdefiniowanie limitu czasu pipeline'u na 30 minut.
- Konfigurację narzędzi Maven, Node.js i Docker.
- Przykładowe zadanie `example-pipeline`.
- Integrację z wtyczkami Configuration as Code i Job DSL.

Wtyczki nie są instalowane przez sam plik YAML. Ich instalację należy wykonać osobno.

## Prompt 2

Wyjaśnij, jak używać tego pliku konfiguracyjnego z Jenkinsem. Podaj kroki instalacji i uruchomienia Jenkinsa z tym szablonem.

## Wyjaśnienie konfiguracji

### 1. Podstawowe ustawienia Jenkins

Sekcja `jenkins` zawiera podstawowe parametry serwera.

`systemMessage` określa komunikat wyświetlany w interfejsie Jenkins.

`numExecutors: 2` ustawia liczbę wykonawców na wbudowanym węźle Jenkins na dwa.

`mode: NORMAL` pozwala przydzielać zadania do węzła zgodnie z jego dostępnością.

Zmienna `BUILD_TIMEOUT_MINUTES` przechowuje wartość 30. Samo jej zdefiniowanie nie wymusza limitu czasu.

Rzeczywisty timeout ustawiono w przykładowym Pipeline:

```groovy
options {
    timeout(time: 30, unit: 'MINUTES')
}
```

### 2. Globalna konfiguracja narzędzi

Sekcja `tool` definiuje narzędzia dostępne w Jenkins.

Maven służy do budowania projektów Java.

Node.js jest wykorzystywany do uruchamiania aplikacji JavaScript i narzędzi npm.

Docker służy do pracy z obrazami i kontenerami.

Przykładowe ścieżki:
- Maven: `/opt/maven`
- Node.js: `/opt/nodejs`
- Docker: `/usr`

Ścieżki należy dostosować do rzeczywistego środowiska.

Zdefiniowanie narzędzia w JCasC nie oznacza jego automatycznej instalacji.

### 3. Wtyczki Jenkins

Do wykorzystania szablonu potrzebne są odpowiednie wtyczki:

- Configuration as Code – odczytywanie konfiguracji YAML.
- Job DSL – tworzenie zadania na podstawie kodu.
- Pipeline – obsługa zadań Pipeline.
- NodeJS – globalna konfiguracja Node.js.
- Docker Commons – integracja narzędzia Docker.
- Maven Integration – dodatkowa integracja Maven, jeżeli jest potrzebna.

Wtyczki należy zainstalować przed zastosowaniem konfiguracji JCasC.

### 4. Przykładowe zadanie Pipeline

Sekcja `jobs` wykorzystuje Job DSL do utworzenia zadania `example-pipeline`.

Zadanie zawiera cztery etapy:

1. Checkout – przykładowe pobieranie kodu.
2. Build – przykładowe budowanie aplikacji.
3. Test – przykładowe uruchamianie testów.
4. Deploy – przykładowe wdrożenie aplikacji.

Etapy wykorzystują polecenie `echo`, dlatego nie wykonują rzeczywistych operacji.

## Instrukcja instalacji i uruchomienia

### Krok 1. Przygotowanie środowiska

Do uruchomienia Jenkinsa można wykorzystać Docker.

Należy mieć zainstalowany Docker Desktop lub Docker Engine.

### Krok 2. Instalacja wtyczek

Przykładowe wymagane identyfikatory wtyczek:

```text
configuration-as-code
job-dsl
workflow-aggregator
nodejs
docker-commons
maven-plugin
```

Wtyczki można zainstalować za pomocą `jenkins-plugin-cli` w obrazie Jenkins lub przez interfejs Manage Jenkins → Plugins.

### Krok 3. Przygotowanie pliku YAML

Plik `jenkins-casc.yaml` należy udostępnić Jenkinsowi.

Przykładowa lokalizacja wewnątrz kontenera:

`/var/jenkins_home/jenkins-casc.yaml`

### Krok 4. Ustawienie zmiennej środowiskowej

Jenkins odczytuje lokalizację konfiguracji z:

`CASC_JENKINS_CONFIG`

Przykładowa wartość:

```text
/var/jenkins_home/jenkins-casc.yaml
```

### Krok 5. Uruchomienie Jenkinsa

Przykładowe polecenie Docker uruchamiane z katalogu zawierającego plik YAML:

```bash
docker run -d --name jenkins-casc -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v "${PWD}/jenkins-casc.yaml:/var/jenkins_home/jenkins-casc.yaml:ro" -e CASC_JENKINS_CONFIG=/var/jenkins_home/jenkins-casc.yaml jenkins/jenkins:lts-jdk21
```

Polecenie pokazuje sposób montowania pliku YAML i ustawienia zmiennej środowiskowej.

Przed użyciem należy przygotować obraz Jenkins z wymaganymi wtyczkami. Standardowy obraz nie gwarantuje ich obecności.

Składnia montowania pliku może wymagać dostosowania do używanego terminala i systemu operacyjnego.

### Krok 6. Otwarcie panelu Jenkins

Po uruchomieniu serwera należy otworzyć:

`http://localhost:8080`

Następnie należy zakończyć wymaganą konfigurację początkową i zalogować się.

### Krok 7. Sprawdzenie konfiguracji

W panelu Jenkins należy przejść do:

Manage Jenkins → Configuration as Code

W tym miejscu można sprawdzić konfigurację i ponownie ją załadować.

Należy również sprawdzić:
- Liczbę wykonawców.
- Konfigurację narzędzi.
- Obecność zadania `example-pipeline`.

## Najlepsze praktyki

1. Przechowywanie konfiguracji JCasC w repozytorium Git.
2. Unikanie zapisywania haseł i tokenów bezpośrednio w YAML.
3. Stosowanie zgodnych wersji Jenkins i wtyczek.
4. Testowanie konfiguracji przed zastosowaniem na produkcji.
5. Regularne aktualizowanie Jenkins i wtyczek.
6. Ograniczanie uprawnień użytkowników i wykonawców.
7. Tworzenie kopii zapasowych konfiguracji.

## Wnioski i obserwacje

AI wygenerowało szablon konfiguracji Jenkins w formacie YAML.

Zastosowanie JCasC pozwala przechowywać konfigurację serwera w repozytorium oraz odtwarzać ją w kolejnych środowiskach.

Dzięki temu administrator nie musi za każdym razem ręcznie ustawiać wszystkich parametrów w interfejsie Jenkins.

Ważne jest jednak wcześniejsze zainstalowanie wymaganych wtyczek i dostosowanie ścieżek narzędzi do konkretnego środowiska.

Zadanie pokazało, że Configuration as Code ułatwia automatyzację zarządzania Jenkinsem i pozwala lepiej kontrolować zmiany w jego konfiguracji.
