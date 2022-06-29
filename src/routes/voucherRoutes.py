from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.redis.voucherController as voucherController

voucher = Blueprint('voucher', __name__)

@voucher.route("/create", methods=['POST'])
@cross_origin()
def create():
	return voucherController.create(request)

@voucher.route("/", methods=['GET'])
@cross_origin()
def index():
	return voucherController.index()

@voucher.route("/show", methods=['GET'])
@cross_origin()
def show():
	return voucherController.show(request.args)

@voucher.route("/update", methods=['PUT'])
@cross_origin()
def update():
	return voucherController.update(request)

@voucher.route("/delete", methods=['DELETE'])
@cross_origin()
def delete():
	return voucherController.delete(request.args)

