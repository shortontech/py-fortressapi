from fortress_api.api_model import ApiModel
from .address_response import AddressResponse


class WireInstructionsResponse(ApiModel):
    account_number = ApiModel.fields.decimal(required=False)
    routing_number = ApiModel.fields.decimal(required=False)
    receiver_name = ApiModel.fields.char(required=False)
    receiver_address = ApiModel.fields.child(related=AddressResponse, required=False)
    receiver_bank_name = ApiModel.fields.char(required=False)
    receiver_bank_address = ApiModel.fields.child(related=AddressResponse, required=False)
    swift_code = ApiModel.fields.char(required=False)
