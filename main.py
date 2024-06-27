import requests

api_key = "b4ee1813a19a450388fce0f020530065"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&" \
      "apiKey=b4ee1813a19a450388fce0f020530065"

# Make request
request = requests.get(url)

# Generated dictionary with data
content = request.json()

# Access article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
