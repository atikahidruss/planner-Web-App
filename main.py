import requests
from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
from config import API_KEY, BASE_URL

API_KEY = "6426bb9f-985b-40a8-b07e-b18ce6da0863"
BASE_URL = "https://holidayapi.com/v1/holidays"

app = Flask(__name__)

# Function to fetch holidays
def fetch_holidays():
    """Fetch holidays for Malaysia in 2023."""
    params = {
        "country": "MY",
        "year": 2023,
        "key": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        holidays = data.get("holidays", [])
        return holidays
    else:
        print(f"Error: {response.status_code}")
        return []

# Route to handle holiday search (AJAX)
@app.route("/search", methods=["GET"])
def search():
    search_query = request.args.get("search", "").lower()
    holidays = fetch_holidays()

    # Filter holidays based on search query
    if search_query:
        holidays = [holiday for holiday in holidays if search_query in holiday["name"].lower() or search_query in holiday["country"].lower()]

    # Return filtered holidays as JSON response
    return jsonify(holidays)

# Route to render payroll page (set as home page)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get input values from the form
        name = request.form.get("name")
        role = request.form.get("role")
        total_days = int(request.form.get("total_days"))
        weekends = int(request.form.get("weekends"))
        holidays = int(request.form.get("holidays"))

        # Calculate total working days
        total_working_days = total_days - weekends - holidays

        # Calculate salary
        salary = total_working_days * 100  # RM100 per day of work

        return render_template("payroll.html", salary=salary, total_working_days=total_working_days)

    return render_template("payroll.html")

# Route to render holidays (calendar)
@app.route("/holidays")
def holidays():
    return render_template("holidays.html")

if __name__ == "__main__":
    app.run(debug=True)
