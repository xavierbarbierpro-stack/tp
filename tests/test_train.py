import os
import joblib
import pandas as pd

def test_model_file_exists():
    # Chemin vers le fichier modèle (à adapter)
    model_path = './data/churn_model_clean.pkl'  # Exemple : .pkl, .h5, .pt, etc.

    # Vérifie que le fichier existe physiquement
    assert os.path.exists(model_path), f"Le fichier modèle '{model_path}' n'existe pas."

    # Optionnel : Teste le chargement du modèle (si applicable)
    try:
        model = joblib.load(model_path)
        assert model is not None, "Le modèle chargé est None."
    except Exception as e:
        raise AssertionError(f"Erreur lors du chargement du modèle : {str(e)}")

def test_no_missing_values():
    # Chemin vers le fichier CSV (à adapter)
    csv_path = './data/customer_churn.csv'

    # 1. Vérifie que le fichier existe
    assert os.path.exists(csv_path), f"Le fichier '{csv_path}' n'existe pas."

    # 2. Charge le CSV dans un DataFrame
    df = pd.read_csv(csv_path)

    # 3. Vérifie qu'il n'y a aucune valeur manquante
    missing_values = df.isna().sum().sum()  # Compte total des NaN
    assert missing_values == 0, (
        f"Le fichier contient {missing_values} valeurs manquantes. "
        f"Voici les colonnes concernées :\n{df.isna().sum()}"
    )

if __name__ == "__main__":
    test_model_file_exists()
    test_no_missing_values()
    print("Tous les tests ont réussi !")
