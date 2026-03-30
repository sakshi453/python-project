import requests
from datetime import date

# ❗ Replace with the API key you get from https://newsapi.org/
API_KEY = "c16b50646cc8437e800aec8d43397cab"


# Base URL for the "everything" endpoint
BASE_URL_EVERYTHING = "https://newsapi.org/v2/everything"
BASE_URL_TOP_HEADLINES = "https://newsapi.org/v2/top-headlines"

# Topics you want daily news about
topics = ["technology", "sports", "health"]

# Today’s date (ISO format yyyy-mm-dd)
today = date.today().isoformat()

for topic in topics:
    # Parameters for searching daily news
    params = {
    "q": topic,
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": API_KEY
}

    # Make HTTP request
    response = requests.get(BASE_URL_EVERYTHING, params=params)

    # Convert to Python dict
    data = response.json()
    print(data)

    # Print summary
    print(f"\n--- {topic.upper()} NEWS ({today}) ---")

    if data.get("status") == "ok":
        articles = data.get("articles", [])
        for i, article in enumerate(articles[:5], start=1):  # only first 5
            title = article.get("title")
            url = article.get("url")
            print(f"{i}. {title}\n   {url}")
    else:
        print("Error:", data.get("message"))
