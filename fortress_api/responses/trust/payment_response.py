from fortress_api.api_model import ApiModel
from .funds_storage_response import FundsStorageResponse

class PaymentResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    """id of the payment"""

    type = ApiModel.fields.char(required=False)
    """type of the payment"""

    status = ApiModel.fields.char(required=False)
    """status of the payment"""

    source = ApiModel.fields.child(related=FundsStorageResponse, required=False)
    """a funds storage response representing the source of the payment"""

    destination = ApiModel.fields.child(related=FundsStorageResponse, required=False)
    """a funds storage response representing the destination of the payment"""

    comment = ApiModel.fields.char(required=False)
    """comment of the payment"""
    funds = ApiModel.fields.decimal(required=False)
    cryptoAmount = ApiModel.fields.decimal(required=False)
    currency = ApiModel.fields.char(required=False)
    sourceCurrency = ApiModel.fields.char(required=False)
    destinationCurrency = ApiModel.fields.char(required=False)
