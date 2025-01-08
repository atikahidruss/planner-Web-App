import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

HOLIDAYS_API_KEY = 'jczwbVvcIbYapoTQPq961w==E7utC5bmVf1oFqe0'
HOLIDAYS_BASE_URL = 'https://api.api-ninjas.com/v1/holidays'

NEWS_API_KEY = '84936d757f71e53eb98cdd42bb4bb240'
NEWS_BASE_URL = 'https://gnews.io/api/v4/search'


def fetch_holidays(year):
    country = 'MY'
    api_url = f'{HOLIDAYS_BASE_URL}?country={country}&year={year}'
    headers = {'X-Api-Key': HOLIDAYS_API_KEY}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        holidays = response.json()
        return [{'name': holiday.get('name'), 'date': holiday.get('date')} for holiday in holidays]
    else:
        print(f"Error fetching holidays: {response.status_code}")
        return []


def fetch_news(query, year, month):
    start_date = f"{year}-{str(month).zfill(2)}-01T00:00:00Z"
    end_date = f"{year}-{str(month + 1).zfill(2)}-01T00:00:00Z" if month < 12 else f"{year + 1}-01-01T00:00:00Z"
    api_url = f"{NEWS_BASE_URL}?q={query}&from={start_date}&to={end_date}&lang=en&token={NEWS_API_KEY}"  # Added lang=en

    response = requests.get(api_url)

    if response.status_code == 200:
        articles = response.json().get('articles', [])
        news_by_date = {}
        for article in articles:
            published_date = article.get('publishedAt', '').split('T')[0]
            if published_date:
                if published_date not in news_by_date:
                    news_by_date[published_date] = []
                news_by_date[published_date].append({
                    "title": article.get("title"),
                    "url": article.get("url")
                })
        print(f"Processed News Data: {news_by_date}")  # Debugging
        return news_by_date
    else:
        print(f"Error fetching news: {response.status_code}, {response.text}")
        return {}


@app.route("/holidays/<int:year>")
def holidays(year):
    holiday_data = fetch_holidays(year)
    return jsonify({'holidays': holiday_data})


@app.route("/news/<int:year>/<int:month>")
def news(year, month):
    news_data = fetch_news("Malaysia OR Kuala Lumpur OR politics OR sport", year, month)
    return jsonify({'news': news_data})


@app.route("/")
def default():
    return render_template("calendar.html")


if __name__ == "__main__":
    app.run(debug=True)
