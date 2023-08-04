from flask import Flask, jsonify, request
from flask_cors import CORS
import aws_controller

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def index():
    return "This is the main page."


@app.route('/get-items', methods=['GET'])
def get_items():
    return jsonify(aws_controller.get_items())


@app.route('/put-item', methods= ['GET','POST'])
def put_item():
    if request.method == 'POST':
        print(request.json)
        data = request.json
        aws_controller.put_item(data['firstName'], data['lastName'], data['date'], data['belt'], data['level'],
                            data['activity'])

        response= data
        #response.headers.add('Access-Control-Allow-Origin', 'https://s3nthr.csb.app')
        print(response)
        return response
    if request.method == 'OPTIONS':
        response =jsonify("CORS check")
        #response.headers.add('Access-Control-Allow-Origin', 'https://s3nthr.csb.app')
        print(response)
        return response
    else:
        return "This is the main page."

if __name__ == '__main__':
    app.run()