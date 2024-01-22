from flask import Flask
from dotenv import load_dotenv
import random
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")
SUPERHEROES = ['SPIDER MAN', 'THOR', 'HULK', 'IRON MAN', 'CAPTAIN AMERICA']


@app.route("/")
def hello_world():
    return f"<h1>Behold, I am {random.choice(SUPERHEROES)}!</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
