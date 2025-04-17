from fortress_api.api_model import ApiModel
from .wallet_response import WalletResponse
from ..meta_response import MetaResponse


class ListWalletsResponse(ApiModel):
    data = ApiModel.fields.list(related=WalletResponse, required=False)
    meta = ApiModel.fields.child(related=MetaResponse, required=False)
