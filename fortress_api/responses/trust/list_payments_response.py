from fortress_api.api_model import ApiModel
from .payment_response import PaymentResponse
from ..listresponse import listresponse


@listresponse(PaymentResponse)
class ListPaymentsResponse(ApiModel):
    pass
