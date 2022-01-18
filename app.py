import os
from flask import Flask
from geekle_api import api_blueprint, current_game

app = Flask(__name__)
app.register_blueprint(api_blueprint)

app.logger.info("Word of the day: " + current_game.get_word_of_the_day())

if __name__ == "__main__":
    debug = os.environ.get("DEBUG", False)
    app.run(debug)
