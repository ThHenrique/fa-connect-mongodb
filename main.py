import src.controllers.userController as userController

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

@app.route("/user", methods=['GET', 'POST'])
@cross_origin()
def user():
	return userController.findQuery()

@app.route("/user/create", methods=['POST'])
@cross_origin()
def userCreate():
	return userController.insert(request)

if __name__ == '__main__':
	app.run(debug=True)