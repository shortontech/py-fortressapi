from fortress_api.api_model import ApiModel
from .funds_storage_response import FundsStorageResponse


class TransactionResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    groupId = ApiModel.fields.char(required=False)
    paymentId = ApiModel.fields.char(required=False)
    paymentType = ApiModel.fields.char(required=False)
    status = ApiModel.fields.char(required=False)
    source = ApiModel.fields.child(related=FundsStorageResponse, required=False)
    destination = ApiModel.fields.child(related=FundsStorageResponse, required=False)
    comment = ApiModel.fields.char(required=False)
    cryptoAmount = ApiModel.fields.decimal(required=False)
    currency = ApiModel.fields.char(required=False)
