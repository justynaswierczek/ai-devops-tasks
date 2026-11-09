
# Zadanie 7: Wygenerowanie prostego skryptu Bash

## Cel zadania

Celem zadania jest wygenerowanie skryptu Bash, który sprawdza, czy usługa Docker jest uruchomiona, a jeśli nie, podejmuje próbę jej uruchomienia.

## Prompt 1

Napisz prosty skrypt bash, który sprawdza, czy usługa Docker działa, a jeśli nie - próbuje ją uruchomić.

## Wygenerowany skrypt

Skrypt zapisano w osobnym pliku `check_docker.sh`.

```bash
#!/bin/bash

if systemctl is-active --quiet docker; then
    echo "Usługa Docker działa."
else
    echo "Usługa Docker nie działa. Próba uruchomienia..."
    sudo systemctl start docker

    if systemctl is-active --quiet docker; then
        echo "Docker został uruchomiony pomyślnie."
    else
        echo "Nie udało się uruchomić Dockera."
        exit 1
    fi
fi
```

## Prompt 2

Wyjaśnij działanie tego skryptu linia po linii, tak jakbyś tłumaczył osobie początkującej.

## Wyjaśnienie działania skryptu

**1. `#!/bin/bash`**

Pierwsza linia informuje system, że skrypt powinien zostać uruchomiony za pomocą interpretera Bash.

**2. `if systemctl is-active --quiet docker; then`**

Instrukcja `if` sprawdza, czy usługa Docker jest aktywna. Polecenie `systemctl is-active` służy do sprawdzania stanu usługi, a opcja `--quiet` powoduje, że wynik nie jest wyświetlany w terminalu.

**3. `echo "Usługa Docker działa."`**

Jeśli Docker jest uruchomiony, skrypt wyświetla odpowiedni komunikat.

**4. `else`**

Ta instrukcja określa, co należy zrobić, jeśli Docker nie jest uruchomiony.

**5. `echo "Usługa Docker nie działa. Próba uruchomienia..."`**

Skrypt informuje użytkownika, że usługa nie działa i zostanie podjęta próba jej uruchomienia.

**6. `sudo systemctl start docker`**

Polecenie próbuje uruchomić usługę Docker. `sudo` umożliwia wykonanie polecenia z uprawnieniami administratora.

**7. `if systemctl is-active --quiet docker; then`**

Po próbie uruchomienia skrypt ponownie sprawdza, czy Docker działa.

**8. `echo "Docker został uruchomiony pomyślnie."`**

Jeśli usługa została uruchomiona, wyświetlany jest komunikat o powodzeniu.

**9. `else`**

Jeżeli Docker nadal nie działa, wykonywana jest kolejna część skryptu.

**10. `echo "Nie udało się uruchomić Dockera."`**

Skrypt informuje użytkownika o nieudanej próbie uruchomienia usługi.

**11. `exit 1`**

Polecenie kończy działanie skryptu z kodem błędu `1`, który oznacza niepowodzenie.

**12. `fi`**

Pierwsze `fi` zamyka wewnętrzną instrukcję warunkową `if`, a drugie zamyka zewnętrzną instrukcję `if`.

## Podsumowanie

Skrypt automatycznie sprawdza stan usługi Docker. Jeśli usługa działa, wyświetla odpowiedni komunikat. Jeśli jest zatrzymana, próbuje ją uruchomić, a następnie ponownie sprawdza jej stan.

Skrypt jest przeznaczony dla systemów Linux korzystających z systemd i może wymagać uprawnień administratora.
