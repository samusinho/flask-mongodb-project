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
        "station": candidate.__dict__
    }), 201