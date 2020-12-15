from flask import Flask, render_template, redirect
import scrape_mars

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)