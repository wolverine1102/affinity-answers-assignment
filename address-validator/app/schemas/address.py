from ..extensions import ma
from marshmallow import Schema, fields, validate

class AddressSchema(ma.Schema):
    address = fields.String(required=True)
    pincode = fields.String(validate=validate.Length(
        equal=6,
        error="PIN Code must be a 6-digit number."
    ))
    city = fields.String()
    state = fields.String()

address_schema = AddressSchema()
