from fortress_api.api_model import ApiModel
from .wallet_transaction_storage_response import WalletTransactionStorageResponse
from .token_response import TokenResponse


class WalletTransactionResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    type = ApiModel.fields.char(required=False)
    source = ApiModel.fields.list(related=WalletTransactionStorageResponse, required=False)
    destination = ApiModel.fields.list(related=WalletTransactionStorageResponse, required=False)
    network = ApiModel.fields.char(required=False)
    assetType = ApiModel.fields.char(required=False)
    token = ApiModel.fields.child(related=TokenResponse, required=False)
    amount = ApiModel.fields.decimal(required=False)
    nft_amount = ApiModel.fields.decimal(required=False)
    gas_price = ApiModel.fields.char(required=False)
    gas_limit = ApiModel.fields.char(required=False)
    network_fee = ApiModel.fields.char(required=False)
    note = ApiModel.fields.char(required=False)
    fail_reason = ApiModel.fields.char(required=False)
    signature = ApiModel.fields.char(required=False)
    rawTx = ApiModel.fields.char(required=False)
    createdAt = ApiModel.fields.datetime(required=False)
