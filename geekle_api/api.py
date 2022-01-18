from flask import Blueprint, jsonify, request, current_app
from .reader import FileReader
from .game import Game

api_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

reader = FileReader("words.txt")
current_game = Game(reader)


@api_blueprint.route("/guess", methods=["POST"])
def guess():
    guess = request.json["guess"]
    current_app.logger.info(f"Player guessed {guess}")
    return jsonify(current_game.guess_word(guess))
