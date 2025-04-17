from fortress_api.api_model import ApiModel
from .wallet_transaction_response import WalletTransactionResponse
from ..meta_response import MetaResponse


class ListWalletTransactionsResponse(ApiModel):
    """List of transactions was successfully retrieved"""
    data = ApiModel.fields.list(related=WalletTransactionResponse, required=False)

    """Gets or sets the data."""
    meta = ApiModel.fields.child(related=MetaResponse, required=False)
