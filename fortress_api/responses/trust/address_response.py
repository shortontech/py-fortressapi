from fortress_api.api_model import ApiModel


class AddressResponse(ApiModel):
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

    def __init__(self, source: dict):
        self.street1 = source.get('street1', '')
        self.street2 = source.get('street2', '')
        self.postal_code = source.get('postalCode', '')
        self.city = source.get('city', '')
        self.state = source.get('state', '')
        self.country = source.get('country', '')
