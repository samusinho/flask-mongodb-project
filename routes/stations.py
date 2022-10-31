from flask import jsonify, request, Blueprint

from controllers.station import StationController
from models.station import StationDoesNotExist

stations_controller = StationController()

stations_bp = Blueprint("stations_blueprint", __name__)

@stations_bp.route("/", methods=["GET"])
def stations():
    list_stations = []
    for station in stations_controller.get_all():
        list_stations.append(station.__dict__)
    return jsonify({
        "stations": list_stations,
        "count": stations_controller.count()
    })

@stations_bp.route("/<string:station_id>", methods=["GET"])
def station(station_id):
    try:
        station = stations_controller.get_by_id()
        return jsonify({ "station": station.__dict__ }), 200
    except StationDoesNotExist:
        return jsonify({
            "error": "Mesa de votación no existe"
        }), 404

@stations_bp.route("/", methods=["POST"])
def create_station():
    station = stations_controller.create(request.get_json())
    return jsonify({
        "message": "Mesa de votación creada exitosamente",
        "station": station.__dict__
    }), 201
