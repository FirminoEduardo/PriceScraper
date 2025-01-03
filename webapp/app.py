from flask import Flask, render_template
from scraper.db_handler import get_products

app = Flask(__name__)

@app.route("/")
def index():
    products = get_products()
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)