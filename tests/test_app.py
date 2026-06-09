import requests

def test_app_is_online():
    url = "http://localhost:5000"  # Remplacez par votre URL

    try:
        response = requests.get(url, timeout=5)  # Timeout de 5 secondes

        # Vérifie que la requête a réussi (statut 200 OK)
        assert response.status_code == 200, (
            f"L'application n'est pas accessible. "
            f"Statut HTTP : {response.status_code}"
        )

    except requests.exceptions.RequestException as e:
        raise AssertionError(f"Impossible de se connecter à l'URL : {str(e)}")

if __name__ == "__main__":
    test_app_is_online()
    print("L'application est en ligne et accessible.")
