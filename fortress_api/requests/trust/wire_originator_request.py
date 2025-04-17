from fortress_api.api_model import ApiModel
from .address_request import AddressRequest


class WireOriginatorRequest(ApiModel):
    """Originator of the wire"""
    name = ApiModel.fields.char(required=False)
    """A Wire Bank sub-object containing information about the wire originator"""
    address = ApiModel.fields.child(related=AddressRequest, required=False)
    """Bank details"""

    def to_request(self):
        response = {}
        if self.name is not None:
            response['name'] = self.name
        if self.address is not None:
            response['address'] = self.address.to_request()
