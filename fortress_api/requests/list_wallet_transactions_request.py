from requests import Response
from fortress_api.api_model import ApiModel
from ..responses.wallet.list_wallet_transactions_response import ListWalletTransactionsResponse


class ListWalletTransactionsRequest(ApiModel):
    status = ApiModel.fields.char(required=False)
    wallet_id = ApiModel.fields.char(required=False)
    page = ApiModel.fields.decimal(required=False)
    page_size = ApiModel.fields.decimal(required=False)

    def to_params(self):
        """Converts the object to a request dictionary"""
        params = {
            'page': self.page,
            'pageSize': min(self.page_size, 50)
        }
        if self.status:
            params['status'] = self.status
        if self.wallet_id:
            params['walletId'] = self.wallet_id
        return params

    def response(self, response: Response):
        """Converts the response to a ListWalletTransactionsResponse"""
        return ListWalletTransactionsResponse(response.json())
