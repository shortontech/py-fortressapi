from fortress_api.api_model import ApiModel
from ..responses.GetCryptoPriceResponse import GetCryptoPriceResponse

class GetCryptoPriceRequest(ApiModel):
    # The PropertyDefinition decorator/attribute is represented here as comments for clarity.

    # to handle such metadata.

    # @PropertyDefinition(required=True, in_='path')
    network = ApiModel.fields.char(required=False)

    # @PropertyDefinition(required=True, in_='path')
    currency = ApiModel.fields.char(required=False)

    # @PropertyDefinition(required=False, in_='body', alias='SpreadBasisPoints')
    spread_basis_points = ApiModel.fields.char(required=False)

    def get_response_instance(self):
        return GetCryptoPriceResponse()

    def submit(self):
        response = super().submit()
        return response

    def get_path(self):
        return f'/api/trust/v1/crypto-currency/crypto-currency-price/{self.network}/{self.currency}'

    def get_method(self):
        return 'GET'
