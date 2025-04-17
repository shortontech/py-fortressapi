from fortress_api.api_model import ApiModel
from fortress_api.responses.trust.payment_response import PaymentResponse


class CreatePaymentRequest(ApiModel):

    def get_response_instance(self):
        return PaymentResponse()

    def submit(self):
        response = super().submit()
        return response

    def get_path(self):
        return '/api/trust/v1/payments'

    def get_method(self):
        return 'POST'
