
/**
 * Pobiera dane użytkownika z API na podstawie jego identyfikatora.
 *
 * Funkcja wysyła żądanie HTTP, sprawdza poprawność odpowiedzi
 * i przekształca otrzymane dane do obiektu użytkownika.
 * W przypadku błędu zapisuje komunikat w konsoli i zwraca null.
 *
 * @param {string|number} userId - Identyfikator użytkownika.
 * @returns {Promise<{name: string, email: string, lastLogin: Date}|null>}
 * Obietnica zwracająca dane użytkownika lub null w przypadku błędu.
 */
function fetchUserData(userId) {
    return fetch(`https://api.example.com/users/${userId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        return {
          name: data.name,
          email: data.email,
          lastLogin: new Date(data.lastLoginTimestamp)
        };
      })
      .catch(error => {
        console.error('Fetch error:', error);
        return null;
      });
  }
  