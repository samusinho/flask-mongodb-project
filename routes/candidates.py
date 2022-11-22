from flask import jsonify, request, Blueprint

from controllers.candidate import CandidateController
from models.candidate import CandidateDoesNotExist

candidates_controller = CandidateController()

candidates_bp = Blueprint("candidates_blueprint", __name__)

@candidates_bp.route("/", methods=["POST"])
def create_candidate():
    candidate = candidates_controller.create(request.get_json())
    return jsonify({
        "message": "Candidato creado exitosamente",
        "candidate": candidate.__dict__
    }), 201

@candidates_bp.route("/", methods=["GET"])
def candidates():
    return jsonify({
        "candidates": [candidate.to_json() for candidate in candidates_controller.get_all()],
        "count": candidates_controller.count()
    })

@candidates_bp.route("/<string:candidate_id>", methods=["GET"])
def candidate(candidate_id):
    try:
        candidate = candidates_controller.get_by_id(candidate_id)
        return jsonify({ "candidate": candidate.to_json() }), 200
    except CandidateDoesNotExist:
        return jsonify({
            "error": "Candidato no existe"
        }), 404

