import requests
import send_email
import os

api_key = os.getenv("NEWS_API_EMAIL_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}"

# Make request
request = requests.get(url)

# Generated dictionary with data
content = request.json()

# Access article titles and description
message = ""
for article in content["articles"]:
    if article["title"] is not None:
        message = message + article["title"] + "\n" + article["description"] + 2*"\n"

message = message.encode("utf-8")
send_email.emailsend(message=message)
