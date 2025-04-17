
from .address_response import AddressResponse
from .wire_bank_data_response import WireBankDataResponse
from fortress_api.api_model import ApiModel


class WireOriginatorResponse(ApiModel):
    """Originator of the wire"""
    name = ApiModel.fields.char(required=False)
    """A Wire Bank sub-object containing information about the wire originator"""
    address = ApiModel.fields.child(related=AddressResponse, required=False)
    """Bank details"""
