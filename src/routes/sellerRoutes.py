from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.sellerController as sellerController

seller = Blueprint('seller', __name__)

@seller.route("/", methods=['GET'])
@cross_origin()
def index():
	return sellerController.index()

@seller.route("/show", methods=['GET'])
@cross_origin()
def show():
	return sellerController.show(request.args)

@seller.route("/create", methods=['POST'])
@cross_origin()
def create():
	return sellerController.create(request)

@seller.route("/update", methods=['PUT'])
@cross_origin()
def update():
	return sellerController.update(request)

@seller.route("/delete", methods=['DELETE'])
@cross_origin()
def delete():
	return sellerController.delete(request.args)


