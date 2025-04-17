from fortress_api.api_model import ApiModel

class ShowPaymentRequest(ApiModel):

    paymentId = ApiModel.fields.char(required=False)
