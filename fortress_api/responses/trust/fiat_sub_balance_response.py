
from fortress_api.api_model import ApiModel


class FiatSubBalanceResponse(ApiModel):
    pendingFromTrade = ApiModel.fields.decimal(required=False)
    lockedPendingFromTrade = ApiModel.fields.decimal(required=False)
