from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from ..schemas.address import address_schema
from ..utils.address import *


address_bp = Blueprint("address", __name__)

@address_bp.route("/address", methods=['POST'])
def validate():
    try:
        data = address_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    
    address = data["address"].lower()
    pincode = extract_pincode(address) if data.get("pincode") is None else data["pincode"]

    if not pincode:
        return jsonify({
            "status": "Error",
            "message": "No PIN Code found in the address."
        }), 400
    
    regions = fetch_regions(pincode)

    if not regions:
        return jsonify({
            "status" : "Error",
            "message": f"PIN Code {pincode} not found"
        }), 400
    
    for region in regions:
        if region["area"] in address and region["district"] in address: 
            return jsonify({
                "status": "Valid",
                "message": "PIN code {pincode} correctly corresponds to {area}, {district}".format(
                    pincode = pincode,
                    area = region["area"].capitalize(),
                    district = region["district"].capitalize()
                )
            }), 200

    return jsonify({
        "status" : "Invalid",
        "message" : f"PIN Code {pincode} does not match the address"
    }), 200
