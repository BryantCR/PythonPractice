#pip install flask
from flask import Flask, jsonify, request

app = Flask(__name__)

#We will append data to this list
data = []

@app.route("/", methods=["GET"])
def read_root():
    return jsonify(data + [{"message": "Welcome to the Flask API"}]), 200

@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "GET":
        return jsonify({"message": "Use POST to add items"}), 200
    
    item = request.json
    data.append({
        "ID": item["ID"],
        "NAME": item["NAME"],
        "ITEMONE": item["ITEMONE"]
    })
    return jsonify({"message": "Item added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True)
