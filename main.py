from flask import Flask

from routes.stations import stations_bp
from routes.party import parties_bp

app = Flask(__name__)

@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "Server running..."
    })

app.register_blueprint(stations_bp, url_prefix="/stations")
app.register_blueprint(parties_bp, url_prefix="/parties")


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
