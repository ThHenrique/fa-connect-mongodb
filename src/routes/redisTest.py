from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.redis.redisController as redisController

redis = Blueprint('redis', __name__)

@redis.route("/", methods=['GET'])
@cross_origin()
def test():
	return redisController.show()

