from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.cassandra.starting as starting

cassandra = Blueprint('cassandra', __name__)

@cassandra.route("/show", methods=['GET'])
@cross_origin()
def show():
	return starting.show()


