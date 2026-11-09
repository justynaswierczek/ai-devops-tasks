# Zadanie 3: Prosty i strukturyzowany prompt

## Prompt 1 (niestrukturyzowany)

```
dockerfile node
```

### Odpowiedź

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

Obraz jest lekki (`alpine`), zależności idą z lockfile (`npm ci`), a pliki `package*.json` są kopiowane przed resztą kodu, żeby przebudowa nie powtarzała instalacji przy każdej zmianie źródła. Port 3000 i `npm start` to przyjęte założenie, bo prompt ich nie podał. W `.dockerignore` warto wykluczyć `node_modules`.

## Prompt 2 (strukturyzowany)

```
Napisz prosty Dockerfile dla aplikacji Node.js, który:
- używa Node 18 jako obrazu bazowego
- kopiuje pliki package.json i package-lock.json
- instaluje zależności
- kopiuje resztę plików aplikacji
- wystawia port 3000
- uruchamia aplikację poleceniem "npm start"
```

### Odpowiedź

```dockerfile
FROM node:18
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

Kolejność jest taka, jak w prompcie: najpierw oba pliki zależności, potem `npm install`, na końcu reszta kodu. `EXPOSE 3000` tylko dokumentuje port — publikuje go dopiero `docker run -p 3000:3000`.

## Porównanie

| | Prompt „dockerfile node” | Prompt ze specyfikacją |
|---|---|---|
| Długość odpowiedzi | Krótki plik plus dopowiedzenie o założeniach | Krótki plik, bez dygresji |
| Wersja Node | Samowolnie `node:20-alpine` | Zgodnie z poleceniem `node:18` |
| Instalacja | `npm ci --omit=dev` | `npm install`, jak w liście kroków |
| Kopiowanie | Glob `package*.json` | Osobno `package.json` i `package-lock.json` |
| Port i start | 3000 i `npm start`, ale to domysł | Wprost z promptu |

Oba pliki są poprawnymi, prostymi Dockerfile i oba kopiują manifest zależności przed kodem. Różnią się tym, co model musiał sobie dośpiewać.

## Wnioski

Niestrukturyzowany prompt daje szybką, często „ładniejszą” propozycję (alpine, `npm ci`), ale wersja Node, port i sposób startu są zgadywane. Gdy zadanie ma konkretne wymagania, taki wynik łatwo je minie — tu Node 20 zamiast 18 i `npm ci` zamiast `npm install`.

Strukturyzowany prompt z listą kroków zwraca plik, który da się odhaczyć punkt po punkcie. Jest mniej miejsca na optymalizacje, których nikt nie prosił, i mniej ryzyka, że obraz nie spełni założeń zadania albo CI.

Do jednorazowej szkicy wystarczy krótki prompt. Do Dockerfile, który ma trafić do repozytorium, warto podać obraz bazowy, kolejność kopiowania, polecenie instalacji, port i komendę startu.
