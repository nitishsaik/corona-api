from flask import Flask
from flask import jsonify
import carona
app = Flask(__name__)
@app.route('/app/api/v1.0/fetch', methods=['GET'])
def index():
    return carona.Json_carona
if __name__=="__main__":
    app.run(threaded=True, port=5000)
