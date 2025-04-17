from fortress_api.api_model import ApiModel
from fortress_api.responses.trust.payment_response import PaymentResponse
from .trade_asset_request import TradeAssetRequest


class TradeRequest(ApiModel):
    idempotencyKey = ApiModel.fields.char(required=False)
    accountId = ApiModel.fields.char(required=False)
    type = ApiModel.fields.char(required=False)
    fromAsset = ApiModel.fields.child(related=TradeAssetRequest, required=False)
    to = ApiModel.fields.child(related=TradeAssetRequest, required=False)
    comment = ApiModel.fields.char(required=False)
    spreadBasisPoints = ApiModel.fields.char(required=False)

    def get_response_instance(self) -> PaymentResponse:
        return PaymentResponse()
