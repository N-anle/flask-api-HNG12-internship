from flask import Flask, Response
from datetime import datetime
import pytz
from flask_cors import CORS
import json


app = Flask(__name__)

CORS(app)

@app.route("/")

def home():
    response_dict = {
        "email" : "bibinusolomon@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url" : "https://github.com/N-anle/flask-api-HNG12-internship"

    }

    response_json = json.dumps(response_dict, ensure_ascii=False)

    return Response(response_json, mimetype="application/json") 


if __name__ == "__main__":
    app.run(debug = True)
