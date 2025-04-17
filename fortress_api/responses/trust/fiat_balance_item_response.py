from fortress_api.api_model import ApiModel
from fortress_api.responses.trust.fiat_sub_balance_response import FiatSubBalanceResponse


class FiatBalanceItemResponse(ApiModel):
    assetType = ApiModel.fields.char(required=False)
    assetFiatType = ApiModel.fields.char(required=False)
    disbursable = ApiModel.fields.decimal(required=False)
    locked = ApiModel.fields.decimal(required=False)
    pending = ApiModel.fields.decimal(required=False)
    total = ApiModel.fields.decimal(required=False)
    subBalances = ApiModel.fields.child(related=FiatSubBalanceResponse, required=False)
