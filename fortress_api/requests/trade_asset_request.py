from fortress_api.api_model import ApiModel


class TradeAssetRequest(ApiModel):
    asset = ApiModel.fields.char(required=False)
    network = ApiModel.fields.char(required=False)
    amount = ApiModel.fields.char(required=False)
