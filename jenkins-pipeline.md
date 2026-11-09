
# Diagram pipeline CI/CD w Jenkins

## Diagram Mermaid

```mermaid
flowchart TD
    A[Checkout kodu] --> B[Budowanie aplikacji]
    B --> C[Testowanie]
    C --> D[Analiza statyczna kodu]
    D --> E[Kontrola bezpieczeństwa]
    E --> F[Budowanie obrazu Docker]
    F --> G[Testy integracyjne]
    G --> H[Wdrożenie na staging]
    H --> I{Czy testy staging przeszły?}
    I -->|Tak| J[Wdrożenie na produkcję]
    I -->|Nie| K[Zatrzymanie pipeline]
    J --> L[Pipeline zakończony sukcesem]
```

## Opis

Diagram przedstawia typowy proces CI/CD w Jenkinsie dla aplikacji webowej.

Pipeline rozpoczyna się od pobrania kodu z repozytorium, a następnie przechodzi przez budowanie aplikacji, testowanie, analizę kodu i kontrolę bezpieczeństwa.

Po pomyślnym zakończeniu tych etapów budowany jest obraz Docker i wykonywane są testy integracyjne.

Następnie aplikacja jest wdrażana na środowisko staging.

Jeżeli testy na staging zakończą się sukcesem, następuje wdrożenie na produkcję. W przeciwnym przypadku pipeline zostaje zatrzymany.
