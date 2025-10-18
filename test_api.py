import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Gender": "female",
    "Age": 45,
    "Height": 1.60,
    "Weight": 95,
    "family_history_with_overweight": "yes",
    "FAVC": "yes",
    "FCVC": 1.0,
    "NCP": 4.0,
    "CAEC": "Frequently",
    "SMOKE": "no",
    "CH2O": 2.0,
    "SCC": "yes",
    "FAF": 0.0,
    "TUE": 1.0,
    "CALC": "Always",
    "MTRANS": "Automobile"
}


response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response:", response.text)
