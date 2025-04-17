
from fortress_api.api_model import ApiModel


class WireBankDataResponse(ApiModel):
    """Bank data for the wire"""
    bankName = ApiModel.fields.char(required=False)
    """name of the bank"""
    accountNumber = ApiModel.fields.char(required=False)
    """account number"""
    routingNumber = ApiModel.fields.char(required=False)
    """routing number"""
    accountType = ApiModel.fields.char(required=False)
