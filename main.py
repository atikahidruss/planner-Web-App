import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

HOLIDAYS_API_KEY = 'jczwbVvcIbYapoTQPq961w==E7utC5bmVf1oFqe0'
HOLIDAYS_BASE_URL = 'https://api.api-ninjas.com/v1/holidays'

NEWS_API_KEY = '4aa5cdf8a3854c278d1f51844ad53692'
NEWS_BASE_URL = 'https://newsapi.org/v2/everything'


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


def fetch_news(year, month):
    country = "Malaysia"
    date_prefix = f"{year}-{str(month).zfill(2)}"
    api_url = f"{NEWS_BASE_URL}?q={country}&from={date_prefix}-01&to={date_prefix}-31&pageSize=100"
    headers = {"Authorization": f"Bearer {NEWS_API_KEY}"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        articles = response.json().get("articles", [])
        news_by_date = {}
        for article in articles:
            published_date = article.get("publishedAt", "").split("T")[0]
            if published_date:
                news_by_date[published_date] = {
                    "url": article.get("url")
                }
        return news_by_date
    else:
        print(f"Error fetching news: {response.status_code}")
        return {}


@app.route("/holidays/<int:year>")
def holidays(year):
    holiday_data = fetch_holidays(year)
    return jsonify({'holidays': holiday_data})


@app.route("/news/<int:year>/<int:month>")
def news(year, month):
    news_data = fetch_news(year, month)
    return jsonify({'news': news_data})


@app.route("/")
def default():
    return render_template("calendar.html")


if __name__ == "__main__":
    app.run(debug=True)
