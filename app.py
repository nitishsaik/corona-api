from flask import Flask
from flask import jsonify
import carona
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return jsonify(carona.d)
if __name__=="__main__":
    app.run(threaded=True, port=5000)
