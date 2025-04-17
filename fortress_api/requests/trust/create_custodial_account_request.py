from fortress_api.api_model import ApiModel
from fortress_api.responses.trust.custodial_account_response import CustodialAccountResponse


class CreateCustodialAccountRequest(ApiModel):
    type = ApiModel.fields.char(required=False)
    personalIdentityId = ApiModel.fields.char(required=False)
    businessIdentityId = ApiModel.fields.char(required=False)
    name = ApiModel.fields.char(required=False)

    def __init__(self, type=None, personalIdentityId=None, businessIdentityId=None, name=None):
        self.type = type
        self.personalIdentityId = personalIdentityId
        self.businessIdentityId = businessIdentityId
        self.name = name

    def get_method(self):
        return 'POST'

    def get_path(self):
        return "/api/trust/v1/custodial-accounts"

    def get_response_instance(self):
        return CustodialAccountResponse()

    def submit(self):
        response = super().submit()
        return response
