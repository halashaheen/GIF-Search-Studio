import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
from GifItem import GifItem  


# Load environment variables from the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    error = None
    gifs = []

    if request.method == "POST":
        query = request.form.get("query", "").strip()
        
        if query:
            url = "https://api.giphy.com/v1/gifs/search"
            params = {
                "api_key": API_KEY,
                "q": query,
                "limit": 3,        # Number of GIFs to return
                "rating": "g"      # Family-friendly GIFs
            }

            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                payload = response.json()

                gifs = [GifItem.from_api_data(item) for item in payload.get("data", [])]
            

            except requests.exceptions.RequestException as e:
                error = f"Failed to retrieve GIFs: {e}"

    return render_template("index.html", gifs=gifs, query=query, error=error)

if __name__ == "__main__":
    app.run(debug=True)
