
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
