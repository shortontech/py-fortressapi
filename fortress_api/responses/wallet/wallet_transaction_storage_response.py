from fortress_api.api_model import ApiModel


class WalletTransactionStorageResponse(ApiModel):
    walletId = ApiModel.fields.char(required=False)
    address = ApiModel.fields.char(required=False)
