from flask import jsonify, request, Blueprint

from controllers.vote import VoteController
from models.vote import VoteDoesNotExist

votes_controller = VoteController()

votes_bp = Blueprint("votes_blueprint", __name__)

@votes_bp.route("/", methods=["POST"])
def create_vote():
    vote = votes_controller.create(request.get_json())
    return jsonify({
        "message": "Voto registrado exitosamente",
        "vote": vote.__dict__
    }), 201

@votes_bp.route("/", methods=["GET"])
def votes():
    return jsonify({
        "votes": [vote.to_json() for vote in votes_controller.get_all()],
        "count": votes_controller.count()
    })

@votes_bp.route("/<string:vote_id>", methods=["GET"])
def vote(vote_id):
    try:
        vote = votes_controller.get_by_id(vote_id)
        return jsonify({"vote": vote.to_json()}), 200
    except VoteDoesNotExist:
        return jsonify({
            "error": "No existe registro de voto"
        }), 404