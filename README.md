# Search and Download YouTube Videos #Shorts

This project allows you to search for YouTube videos based on a specific theme and save the videos found in a JSON file for later download.

The script uses the YouTube Data v3 API to search and retrieve videos with a hashtag `#shorts` and a short duration. The JSON file generated contains video IDs and titles.

## Prerequisites

Before you can run the script, you need to have installed the following dependencies:

- Python 3** : The script is written in Python 3.
- Google API Client Library**: Used to interact with the YouTube Data v3 API.

### Installing dependencies

1. Clone this repository or download the source code to your machine.
2. Install the necessary dependencies with `pip` :

    ``bash
    pip install google-api-python-client
    ```
    
## Configuration

1. **YouTube API**: You need to generate a YouTube API key by following the steps below:
   - Go to [Google Developers Console](https://console.developers.google.com/).
   - Create a project and activate the YouTube Data v3 API.
   - Generate an API key and replace the value `YOUTUBE_API_KEY` in the script with your key.

2. **Search**: Specify the search theme by modifying the `SEARCH_QUERY` variable in the script. For example, you can search for videos related to a specific topic such as “tech”, “gaming”, etc.

3. **Max Results**: Modify the `MAX_RESULTS` variable to define the maximum number of results to be retrieved (up to 50).

## Usage

### Running the script

1. Modify the following values in the script:
   - `YOUTUBE_API_KEY`: Add your YouTube API key.
   - SEARCH_QUERY`: Specify the search theme.
   - `MAX_RESULTS`: Set the maximum number of videos to be retrieved (default 10).

2. Run the script to search for YouTube videos and save the results in a JSON file.
