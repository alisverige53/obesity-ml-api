from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Ladda modellen och klasserna
model = joblib.load("models/basta_pipeline.pkl")
classes = joblib.load("models/klasser.pkl")

@app.route("/")
def home():
    return "Weight Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])

        # Gör prediktion
        prediction = model.predict(df)

        # Konvertera NumPy-int64 till vanlig int
        index = int(prediction[0])

        # Hämta motsvarande viktklass
        result = classes[index]

        # Returnera JSON-svar
        return jsonify({"prediction": str(result)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
