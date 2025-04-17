from fortress_api.api_model import ApiModel


class AddressRequest(ApiModel):
    street1 = ApiModel.fields.char(required=False)
    """Second line of the street address"""
    street2 = ApiModel.fields.char(required=False)
    """First line of the street address"""
    postal_code = ApiModel.fields.char(required=False)
    """Postal code."""
    city = ApiModel.fields.char(required=False)
    """City"""
    state = ApiModel.fields.char(required=False)
    """State or Province"""
    country = ApiModel.fields.char(required=False)
    """Two digit country code"""

    def to_request(self):
        result = {}
        if self.street1 is not None:
            result['street1'] = self.street1
        if self.street2 is not None:
            result['street2'] = self.street2
        if self.postal_code is not None:
            result['postalCode'] = self.postal_code
        if self.city is not None:
            result['city'] = self.city
        if self.state is not None:
            result['state'] = self.state
        if self.country is not None:
            result['country'] = self.country
        return result
