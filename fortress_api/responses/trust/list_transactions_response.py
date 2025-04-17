from fortress_api.api_model import ApiModel
from .transaction_response import TransactionResponse
from ..listresponse import listresponse

@listresponse(TransactionResponse)
class ListTransactionsResponse(ApiModel):
    pass
