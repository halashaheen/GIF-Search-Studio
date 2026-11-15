import os
import requests
from dotenv import load_dotenv
from GifItem import GifItem  

input_query = input("Enter a search query for GIFs: ").strip()
search_query = input_query if input_query else "funny cats"  # Default query if none provided

# Load environment variables from the .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv("API_KEY") 


# Define the API endpoint and parameters
url = "https://api.giphy.com/v1/gifs/search"
params = {
    "api_key": API_KEY,
    "q": search_query,  # Search query for GIFs
    "limit": 2,  # number of GIFs to return
    "rating": "g"  # g stands for General Audiences, family-friendly GIFs suitable for all ages
}

# Send the GET request

response = requests.get(url, params=params)
response.raise_for_status()  # Raises an error for bad status codes


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parses the JSON response into a Python dictionary
    payload = response.json()  
    

    try:
        gifs = [GifItem.from_api_data(item) for item in payload.get("data", [])]

        print(f"\n=== Giphy Search Summary for '{search_query}' ===")
        print(f"Total Results Retrieved: {len(gifs)}\n")

        if not gifs:
            print("No GIFs found matching your query.")
        else:
            for idx, gif in enumerate(gifs, start=1):
                print(gif.display_summary(idx))

    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
    except ValueError as e:
        print(f"Configuration Error: {e}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
