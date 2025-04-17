from fortress_api.api_model import ApiModel
from .custodial_account_response import CustodialAccountResponse
from ..listresponse import listresponse

@listresponse(CustodialAccountResponse)
class ListCustodialAccountsResponse(ApiModel):
    pass
