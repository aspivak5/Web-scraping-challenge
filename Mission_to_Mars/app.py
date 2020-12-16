from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

@app.route("/")
def main():
    mars = mongo.db.collection.find_one()

    return render_template("index.html", mars_data=mars)

@app.route("/scrape")
def scrape():
    # mars = mongo.db.collection
    mars_data = scrape_mars.scrape_info()
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)