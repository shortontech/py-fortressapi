from fortress_api.api_model import ApiModel
from ...responses.trust.list_custodial_accounts_response import ListCustodialAccountsResponse
from requests import Response

class ListCustodialAccountsRequest(ApiModel):
    owner_identity_id = ApiModel.fields.decimal(required=False)
    page = ApiModel.fields.decimal(required=False)
    page_size = ApiModel.fields.decimal(required=False)

    def to_params(self):
        """Converts the object to a request dictionary"""
        return {
            "page": self.page,
            "pageSize": self.page_size
        }
