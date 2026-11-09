# Zadanie 4: Określanie roli w promptach

## Pytanie

Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

## Jak zbierano odpowiedzi

Zadanie wykonano w ChatGPT, ponieważ w Claude skończył się dostępny limit wiadomości. Zadano dwa pytania dotyczące tego samego problemu. Pierwsze pytanie było ogólne, natomiast w drugim przypisano modelowi rolę doświadczonego DevOps Engineera z 10-letnim doświadczeniem.

Celem było sprawdzenie, czy przypisanie roli wpływa na szczegółowość i specjalistyczny charakter odpowiedzi.

## Odpowiedź 1: Bez przypisanej roli

**Prompt:**

Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

**Odpowiedź ChatGPT:**

Duże zużycie pamięci przez kontener Docker można ograniczyć na kilka sposobów:

1. **Sprawdzenie zużycia pamięci.** Polecenie `docker stats` pozwala sprawdzić, ile pamięci RAM wykorzystują poszczególne kontenery.
2. **Ustawienie limitu pamięci.** Można ograniczyć pamięć dostępną dla kontenera, np. `docker run --memory=512m nazwa_obrazu`.
3. **Sprawdzenie logów.** Polecenie `docker logs nazwa_kontenera` może pomóc w znalezieniu błędów aplikacji.
4. **Optymalizacja aplikacji.** Warto sprawdzić, czy aplikacja nie przechowuje niepotrzebnych danych w pamięci.
5. **Ponowne uruchomienie kontenera.** Restart może tymczasowo pomóc, ale nie rozwiąże problemu, jeśli przyczyną jest np. wyciek pamięci.

## Odpowiedź 2: Z przypisaną rolą

**Prompt:**

Jesteś doświadczonym DevOps Engineerem z 10-letnim doświadczeniem. Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

**Odpowiedź ChatGPT:**

Problem dużego zużycia pamięci przez kontener Docker najlepiej rozwiązywać etapami, zaczynając od diagnostyki.

1. **Monitorowanie zasobów.** Uruchom `docker stats`, aby sprawdzić aktualne wykorzystanie RAM i CPU.
2. **Analiza procesów.** Użyj `docker top nazwa_kontenera`, aby sprawdzić procesy uruchomione wewnątrz kontenera.
3. **Weryfikacja błędów OOM.** Polecenie `docker inspect nazwa_kontenera` pozwala sprawdzić pole `State.OOMKilled`, które informuje, czy kontener został zakończony z powodu braku pamięci.
4. **Konfiguracja limitów.** Ustaw limit RAM za pomocą parametru `--memory`, a w razie potrzeby skonfiguruj również `--memory-swap`.
5. **Analiza aplikacji.** Sprawdź możliwe wycieki pamięci, wielkość cache oraz konfigurację garbage collectora.
6. **Długoterminowe monitorowanie.** W większych środowiskach warto wykorzystać Prometheus i Grafana do zbierania metryk i wykrywania nietypowych wzrostów zużycia pamięci.

## Porównanie odpowiedzi

Pierwsza odpowiedź była krótsza i bardziej ogólna. Przedstawiała podstawowe sposoby rozwiązania problemu, takie jak sprawdzenie zużycia RAM, ustawienie limitów czy restart kontenera.

Druga odpowiedź była bardziej techniczna. Zawierała dodatkowe polecenia diagnostyczne, informacje o błędach OOM oraz propozycję monitorowania zasobów za pomocą Prometheus i Grafana.

## Wnioski i obserwacje

Przypisanie modelowi roli DevOps Engineera wpłynęło na charakter odpowiedzi. Druga odpowiedź była bardziej szczegółowa, uporządkowana i zawierała więcej specjalistycznych informacji.

Na podstawie tego przykładu można zauważyć, że określenie roli w prompcie może pomóc uzyskać odpowiedź lepiej dopasowaną do konkretnego zadania. Nie gwarantuje jednak, że odpowiedź będzie zawsze poprawniejsza.