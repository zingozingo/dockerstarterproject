from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    country = request.form.get("country")
    print("Received city:", city, "country:", country)
    if not city:
        return jsonify({"error": "Please enter a city!"})
    query = f"{city},{country}" if country else city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    print("API response status:", response.status_code, "Data:", response.json())
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "City not found or API error!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)