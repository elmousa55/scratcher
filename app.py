from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def receive_stock_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Process the received data here
    print(data)

    # Respond back
    return jsonify({"status": "success", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)
