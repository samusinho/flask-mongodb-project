from flask import jsonify, request, Blueprint, make_response

from controllers.party import PartyController
from models.party import PartyDoesNotExist

parties_controller = PartyController()

parties_bp = Blueprint("parties_blueprint", __name__)

@parties_bp.route("/", methods=["GET"])
def parties():
    list_parties = []
    for party in parties_controller.get_all():
        list_parties.append(party.__dict__)
    return jsonify({
        "parties": list_parties,
        "count": parties_controller.count()
    })

@parties_bp.route("/<string:party_id>", methods=["GET"])
def party(party_id):
    try:
        party = parties_controller.get_by_id(party_id)
        return make_response({ "party": party.__dict__ }, 200)
    except PartyDoesNotExist:
        return jsonify({
            "error": "Partido político no existe"
        }), 404

@parties_bp.route("/", methods=["POST"])
def create_party():
    party = parties_controller.create(request.get_json())
    return jsonify({
        "message": "Partido político creado exitosamente",
        "party": party.__dict__
    }), 201

@parties_bp.route("/<string:party_id>", methods=["PUT"])
def update_party(party_id):
    try:
        party = parties_controller.update(party_id, request.get_json())
        return jsonify(party.to_json())
    except PartyDoesNotExist:
        return jsonify({
            "message": "Partido político no encontrado"
        }), 404



