# GIF Search Studio

A simple Python web application that interacts with a public GIF API endpoint, allowing users to search for GIFs and render the results dynamically on an HTML page.

## Features

- **GIF Search:** Query a public GIF API endpoint using custom search terms.
- **Object-Oriented Modeling:** Encapsulates GIF metadata and media URLs using a dedicated `GifItem` model.
- **Web Interface:** Renders search results cleanly through HTML templates.

<video src="https://github.com/halashaheen/GIF-Search-Studio/blob/main/GIFs/GIF-1.mp4" controls="controls" style="max-width: 730px;">
</video>


## Project Structure

```text
GIF-Search-Studio/
├── templates/          # HTML templates for rendering the search interface and results
├── GifItem.py          # Data model class representing individual GIF items
├── app.py              # Web application routes and request handling
├── main.py             # Application entry point
└── requirements.txt    # Python dependencies
```

## Prerequisites

- Python 3.11 or higher
- A valid API key for the GIF service (e.g., Giphy or Tenor)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/halashaheen/GIF-Search-Studio.git
   ```

2. **Create and activate a virtual environment (optional):**
   ```bash
    uv venv C:\Users\user\iti-athar --python 3.12
    C:\Users\user\iti-athar\Scripts\Activate.ps1 
   ```

3. **Install dependencies:**
   ```bash
    uv pip install -r requirements.txt
   ```

## Configuration

Set up your GIF API key as an environment variable (or update your configuration file as defined in `app.py` / `main.py`):

```bash
 set GIF_API_KEY=your_api_key_here
```

## Usage

1. **Start the application:**
   ```bash
    python .\app.py 
   ```
   *(If using Flask directly via `app.py`, run `flask run` or `python app.py`)*

2. **Open in your browser:**
   Navigate to `http://127.0.0.1:5000` (or the port specified in your terminal) to start searching for GIFs.


 
