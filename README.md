# Recherche et Téléchargement de Vidéos YouTube #Shorts

Ce projet permet de rechercher des vidéos YouTube basées sur un thème spécifique et de sauvegarder les vidéos trouvées dans un fichier JSON pour téléchargement ultérieur.

Le script utilise l'API YouTube Data v3 pour effectuer des recherches et récupérer des vidéos avec un hashtag `#shorts` et une durée courte. Le fichier JSON généré contient les identifiants et les titres des vidéos.

## Prérequis

Avant de pouvoir exécuter le script, vous devez avoir installé les dépendances suivantes :

- **Python 3** : Le script est écrit en Python 3.
- **Google API Client Library** : Utilisé pour interagir avec l'API YouTube Data v3.

### Installation des dépendances

1. Clonez ce dépôt ou téléchargez le code source sur votre machine.
2. Installez les dépendances nécessaires avec `pip` :

    ```bash
    pip install google-api-python-client
    ```

## Configuration

1. **API YouTube** : Vous devez générer une clé API YouTube en suivant les étapes suivantes :
   - Allez sur [Google Developers Console](https://console.developers.google.com/).
   - Créez un projet et activez l'API YouTube Data v3.
   - Générez une clé API et remplacez la valeur `YOUTUBE_API_KEY` dans le script avec votre clé.

2. **Recherche** : Spécifiez le thème de recherche en modifiant la variable `SEARCH_QUERY` dans le script. Par exemple, vous pouvez rechercher des vidéos liées à un sujet spécifique comme "tech", "gaming", etc.

3. **Résultats Max** : Modifiez la variable `MAX_RESULTS` pour définir le nombre maximum de résultats à récupérer (jusqu'à 50).

## Utilisation

### Exécution du script

1. Modifiez les valeurs suivantes dans le script :
   - `YOUTUBE_API_KEY` : Ajoutez votre clé API YouTube.
   - `SEARCH_QUERY` : Spécifiez le thème de recherche.
   - `MAX_RESULTS` : Définissez le nombre maximum de vidéos à récupérer (par défaut 10).

2. Exécutez le script pour rechercher des vidéos YouTube et sauvegarder les résultats dans un fichier JSON.

   ```bash
   python search_youtube.py
