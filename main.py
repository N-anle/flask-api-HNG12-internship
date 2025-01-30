from flask import Flask, request, jsonify
from datetime import datetime
import pytz
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")

def home():
    response = {
        "email" : "bibinusolomon@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url" : "https://github.com/N-anle/flask-api-HNG12-internship"

    }

    return jsonify(response)    


if __name__ == "__main__":
    app.run(debug = True)