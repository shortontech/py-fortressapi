from fortress_api.api_model import ApiModel

class WireSimulatedRequest(ApiModel):
    custodial_account_id = ApiModel.fields.decimal(required=False)
    amount: ApiModel.fields.decimal(required=False)
    origin = ApiModel.fields.char(required=False)
    comment = ApiModel.fields.char(required=False)

    def to_request(self):
        """Converts the object to a request dictionary"""
        return {
            "amount": self.amount,
            "origin": self.origin
        }
