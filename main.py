import requests
import send_email
import os

api_key = os.getenv("NEWS_API_EMAIL_KEY")
topic = "Ravish Kumar"
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&"\
      "language=en"

# Make request
request = requests.get(url)

# Generated dictionary with data
content = request.json()
message = "Subject : Daily NewsFlash" + "\n"
# Access article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        message = message + article["title"] + "\n" \
                  + article["description"] + "\n" \
                  + article["url"] + 2*"\n"

message = message + "**If you don't receive the messages on the scheduled "\
                    "NewsFlash time, then either reply to the previous"\
                    "one addressing the concern or contact the admin.**"


encoded_message = message.encode("utf-8")
send_email.emailsend(message=encoded_message)
