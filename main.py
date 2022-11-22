from flask import Flask
from flask_cors import CORS

from routes.stations import stations_bp
from routes.parties import parties_bp
from routes.candidates import candidates_bp
from routes.votes import votes_bp

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "Server running..."
    })

app.register_blueprint(stations_bp, url_prefix="/stations")
app.register_blueprint(parties_bp, url_prefix="/parties")
app.register_blueprint(candidates_bp, url_prefix="/candidates")
app.register_blueprint(votes_bp, url_prefix="/votes")

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
