
# Zadanie 6: Pierwszy diagram Mermaid

## Prompt

Stwórz prosty diagram Mermaid pokazujący proces CI/CD: commit → build → test → deploy.

## Wygenerowany kod Mermaid

```mermaid
flowchart LR
    A[Commit] --> B[Build]
    B --> C[Test]
    C --> D[Deploy]
```

## Opis wygenerowanego diagramu

Diagram przedstawia podstawowy proces CI/CD składający się z czterech etapów:

1. **Commit** – zapisanie zmian w repozytorium kodu.
2. **Build** – zbudowanie aplikacji.
3. **Test** – sprawdzenie poprawności działania aplikacji.
4. **Deploy** – wdrożenie aplikacji.

Diagram ma układ poziomy. Poszczególne etapy są przedstawione jako prostokątne bloki połączone strzałkami, które wskazują kolejność wykonywania działań.

## Obserwacje

Kod Mermaid pozwala w prosty sposób stworzyć czytelny diagram bez korzystania z narzędzi graficznych. Diagram można wyświetlić i edytować w Mermaid Live Editor.
