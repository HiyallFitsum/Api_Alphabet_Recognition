from flask import jsonify, requests, Flask
from classifier.py import get_prediction

app = Flask()

    @app.route("/predict-alphabet", methods=["POST"])
    def predict_data():
        image = request.files.get("alphabet")
        prediction = get_prediction(image)
        return jsonify({
            "prediction": prediction
        }), 200

get_prediction()
predict_data() 