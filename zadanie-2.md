# Zadanie 2: Porównanie odpowiedzi różnych modeli

## Pytanie

Wymień 5 korzyści z używania kontenerów Docker w środowisku programistycznym.

## Jak zbierano odpowiedzi

W panelu agenta Cursor model jest ustawiony na **Grok 4.7** i oznaczony kłódką. Kliknięcie nazwy modelu oraz skrót Ctrl+/ nie otwierają listy modeli. Zamiast tego pojawia się komunikat: „Upgrade to unlock more models. More models are only available on paid plans.”

Próba zadania tego samego pytania osobnym agentom (Claude Sonnet, GPT oraz Grok 4.6) została odrzucona: na planie Free wybór innego modelu jest niedostępny. Dlatego poniżej jest jedna rzeczywista odpowiedź. Drugiej niezależnej odpowiedzi nie udało się zebrać, więc nie porównuję tu wymyślonych tekstów.

## Odpowiedź: Grok 4.7

1. **To samo środowisko u każdego.** Kontener zawiera aplikację i jej zależności (wersję Pythona, Node, biblioteki systemowe), więc projekt startuje tak samo na laptopie, u kolegi z zespołu i w CI. Kończy się klasyczne „u mnie działa”.
2. **Szybkie stawianie zależności.** Baza, kolejka czy cache (PostgreSQL, Redis, RabbitMQ) wstają jedną komendą `docker compose up`, bez ręcznej instalacji na systemie.
3. **Izolacja od systemu hosta.** Procesy i pakiety żyją w kontenerze, więc eksperyment z inną wersją biblioteki nie psuje narzędzi zainstalowanych globalnie.
4. **Bliskość do produkcji.** Ten sam obraz, który deweloper buduje lokalnie, może iść dalej do testów i na serwer. Mniej niespodzianek wynika z różnic między środowiskami.
5. **Łatwe sprzątanie i powrót do znanego stanu.** Usunięcie kontenera kasuje stan eksperymentu. Nowy start z obrazu albo z volume jest powtarzalny i nie zostawia śmieci w systemie.

Odpowiedź jest krótka: pięć punktów, każdy z konkretnym przykładem narzędzia albo sytuacji (Compose, PostgreSQL, Redis, ten sam obraz na CI i produkcji).

## Odpowiedź drugiego modelu

Brak. Selektor modelu w tym czacie jest zablokowany, a konto nie pozwala uruchomić drugiego modelu.

## Podsumowanie różnic

Różnic w szczegółowości, długości i przykładach nie da się uczciwie opisać, bo jest tylko jedna odpowiedź. Żeby dokończyć porównanie, potrzebny jest drugi model (plan z odblokowanym selektorem albo wklejenie odpowiedzi z innego czatu). Wtedy warto zestawić liczbę zdań, czy pojawiają się konkretne komendy i czy przykłady dotyczą lokalnej pracy, czy także CI i produkcji.
