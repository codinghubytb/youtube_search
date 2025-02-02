import os
import json
from googleapiclient.discovery import build

# Configuration
YOUTUBE_API_KEY = ""
SEARCH_QUERY = ""  # Theme précis
MAX_RESULTS = 10  # Nombre max de résultats de recherche
DOWNLOADED_FILE = "downloaded_videos.json"  # Fichier pour suivre les vidéos téléchargées

# Créer un client YouTube
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# Charger les vidéos déjà téléchargées
if os.path.exists(DOWNLOADED_FILE):
    with open(DOWNLOADED_FILE, "r") as f:
        downloaded_videos = json.load(f)
else:
    downloaded_videos = []

# Recherche de vidéos sur YouTube
def search_youtube(query, max_results):
    request = youtube.search().list(
        q=f"{query} #shorts",  # Combinaison de la requête de recherche et du hashtag
        part="id,snippet",
        type="video",
        maxResults=max_results,
        videoDuration="short",
        order="viewCount"
    )

    response = request.execute()
    return response.get("items", [])

# Fonction principale
def main():
    videos = search_youtube(SEARCH_QUERY, MAX_RESULTS)
    video_data = []
    for video in videos:
        video_id = video["id"]["videoId"]
        title = video["snippet"]["title"]
        
        # Ajouter la vidéo aux résultats
        video_data.append({"video_id": video_id, "title": title})
    
    # Sauvegarder les vidéos trouvées dans un fichier JSON
    with open("videos_to_download.json", "w") as f:
        json.dump(video_data, f)

if __name__ == "__main__":
    main()
