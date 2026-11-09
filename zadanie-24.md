
# Zadanie 24: Interpretacja danych wydajnościowych

## Cel zadania

Celem zadania jest wykorzystanie AI do analizy metryk wydajnościowych serwera API, zidentyfikowania potencjalnych problemów oraz zaproponowania sposobów poprawy wydajności.

## Dane wejściowe

Metryki serwera API z ostatnich 24 godzin:

- Średni czas odpowiedzi: 230 ms
- 95. percentyl czasu odpowiedzi: 450 ms
- 99. percentyl czasu odpowiedzi: 1200 ms
- Liczba zapytań: 15 000
- Liczba błędów 5xx: 120
- Użycie CPU: średnio 45%, maksymalnie 80%
- Użycie pamięci: średnio 2,1 GB, maksymalnie 3,5 GB (z 4 GB dostępnych)

## Prompt

Zinterpretuj te dane. Czy widzisz jakieś potencjalne problemy? Co sugerujesz, aby poprawić wydajność?

## Odpowiedź ChatGPT

### 1. Analiza czasu odpowiedzi

Średni czas odpowiedzi wynosi 230 ms, co może być akceptowalnym wynikiem dla wielu aplikacji API.

Jednak 95. percentyl wynosi 450 ms, a 99. percentyl aż 1200 ms.

Oznacza to, że:
- 95% zapytań ma czas odpowiedzi nieprzekraczający około 450 ms.
- 99% zapytań ma czas odpowiedzi nieprzekraczający około 1200 ms.
- Około 1% najwolniejszych zapytań trwa co najmniej 1200 ms.

Wskazuje to na występowanie pojedynczych znacznie wolniejszych odpowiedzi, które mogą negatywnie wpływać na doświadczenia użytkowników.

### 2. Analiza liczby błędów

W ciągu 24 godzin serwer obsłużył 15 000 zapytań, z czego 120 zakończyło się błędem 5xx.

Wskaźnik błędów wynosi:

`120 / 15000 * 100% = 0,8%`

Oznacza to, że około 0,8% wszystkich zapytań zakończyło się błędem serwera.

Błędy 5xx mogą wskazywać na problemy z aplikacją, bazą danych, przeciążeniem lub komunikacją z innymi usługami.

### 3. Analiza wykorzystania CPU

Średnie wykorzystanie procesora wynosi 45%, a maksymalne 80%.

Oznacza to, że serwer nie jest stale przeciążony, ale w niektórych momentach wykorzystanie CPU jest stosunkowo wysokie.

Warto sprawdzić, czy wzrost wykorzystania procesora pokrywa się z wydłużonym czasem odpowiedzi lub występowaniem błędów.

### 4. Analiza wykorzystania pamięci RAM

Średnie wykorzystanie pamięci wynosi 2,1 GB z dostępnych 4 GB, czyli 52,5%.

Maksymalne wykorzystanie wynosi 3,5 GB, czyli 87,5%.

Oznacza to, że w momentach największego obciążenia pozostaje jedynie około 0,5 GB wolnej pamięci.

Może to zwiększać ryzyko problemów z pamięcią, szczególnie gdy jej zużycie będzie nadal rosło.

## Zidentyfikowane potencjalne problemy

**1. Wysoki czas odpowiedzi dla najwolniejszych zapytań**

99. percentyl wynosi 1200 ms, co oznacza, że część użytkowników może doświadczać wyraźnych opóźnień.

**2. Występowanie błędów serwera**

Wskaźnik błędów 5xx na poziomie 0,8% może wskazywać na problemy ze stabilnością aplikacji.

**3. Wysokie maksymalne wykorzystanie pamięci**

Zużycie 87,5% dostępnej pamięci RAM pozostawia niewielki zapas na dodatkowe obciążenie.

**4. Okresowe wzrosty wykorzystania CPU**

Maksymalne użycie CPU wynoszące 80% może wskazywać na okresowe zwiększenie obciążenia serwera.

## Propozycje poprawy wydajności

### 1. Optymalizacja zapytań do bazy danych

Warto przeanalizować najwolniejsze zapytania SQL lub operacje na bazie danych.

Można zastosować odpowiednie indeksy i ograniczyć liczbę niepotrzebnych zapytań.

### 2. Wdrożenie mechanizmu cache

Często pobierane dane można przechowywać w pamięci podręcznej, np. Redis.

Pozwoli to ograniczyć liczbę operacji na bazie danych i skrócić czas odpowiedzi.

### 3. Analiza błędów 5xx

Należy sprawdzić logi aplikacji i ustalić, które endpointy najczęściej zwracają błędy.

Warto również sprawdzić, czy błędy pojawiają się w godzinach największego obciążenia.

### 4. Monitorowanie pamięci RAM

Należy obserwować zużycie pamięci w dłuższym okresie i sprawdzić, czy nie występują wycieki pamięci.

W razie potrzeby można zoptymalizować aplikację lub zwiększyć dostępną pamięć RAM.

### 5. Monitorowanie CPU i obciążenia

Warto sprawdzić, które procesy najbardziej obciążają procesor oraz czy występuje zależność między użyciem CPU a czasem odpowiedzi.

Jeżeli aplikacja będzie regularnie osiągała wysokie wykorzystanie zasobów, można rozważyć skalowanie serwera.

### 6. Wdrożenie monitoringu

Do monitorowania wydajności można wykorzystać narzędzia takie jak Prometheus i Grafana.

Pozwolą one śledzić czasy odpowiedzi, wykorzystanie zasobów i liczbę błędów oraz szybciej wykrywać problemy.

## Podsumowanie analizy

| Metryka | Wartość | Ocena |
|---|---|---|
| Średni czas odpowiedzi | 230 ms | Potencjalnie akceptowalny |
| 95. percentyl | 450 ms | Wymaga obserwacji |
| 99. percentyl | 1200 ms | Możliwe problemy z opóźnieniami |
| Liczba zapytań | 15 000 | Brak podstaw do oceny bez kontekstu |
| Błędy 5xx | 0,8% | Wymagają analizy |
| CPU średnie | 45% | Umiarkowane wykorzystanie |
| CPU maksymalne | 80% | Okresowo wysokie |
| RAM maksymalne | 87,5% | Niewielki zapas pamięci |

Ocena metryk zależy od wymagań aplikacji, przyjętych limitów wydajnościowych i charakterystyki ruchu.

## Wnioski i obserwacje

Analiza wykazała, że serwer API nie jest stale przeciążony, jednak występują potencjalne problemy związane z czasem odpowiedzi, błędami 5xx oraz wysokim maksymalnym wykorzystaniem pamięci RAM.

W pierwszej kolejności warto przeanalizować przyczyny błędów serwera oraz najwolniejsze zapytania. Następnie można rozważyć optymalizację bazy danych, zastosowanie cache i poprawę monitoringu.

AI pomogło zinterpretować dane wydajnościowe i wskazać obszary wymagające dalszej analizy.

Zadanie pokazało, że na podstawie podstawowych metryk można zidentyfikować potencjalne problemy, jednak do ustalenia ich dokładnych przyczyn potrzebne są bardziej szczegółowe dane i logi.
