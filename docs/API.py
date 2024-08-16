!pip install flask
!ngrok config add-authtoken 2ke9C5yBTSp1duXvdhc8EweaieW_7w2mjTxbEnrP4qsJHjNhA
from flask import Flask, request, jsonify
from pyngrok import ngrok
import threading

app = Flask(_name_)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json['query']
    sql_query_str = "SELECT * FROM users WHERE signup_date > '2024-01-01'"
    return jsonify({'sql_query': sql_query_str})

def run():
    app.run(host='0.0.0.0', port=5000)

# Create ngrok tunnel
url = ngrok.connect(5000)
print('Public URL:', url)

# Run the Flask server in a separate thread
thread = threading.Thread(target=run)
thread.start()
#testing import requests
#url = "https://10dc-34-106-241-42.ngrok-free.app/predict"
#data = {"query": "Show me all users who signed up last week"}
#response = requests.post(url, json=data)
#print(response.json())
