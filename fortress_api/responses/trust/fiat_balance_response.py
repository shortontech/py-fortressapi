from fortress_api.api_model import ApiModel
from fortress_api.responses.trust.fiat_balance_item_response import FiatBalanceItemResponse


class FiatBalanceResponse(ApiModel):
    def __init__(self):
        super().__init__()
        self.data = None  # Use Python's None instead of mixed

    def response(self, response):
        return self.of(FiatBalanceItemResponse)

    def get_response_instance(self):
        return self.of(FiatBalanceItemResponse)
