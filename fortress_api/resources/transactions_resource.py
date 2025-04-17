from .fortress_resource import FortressResource
from ..responses.trust.transaction_response import TransactionResponse
from ..requests.trust import ListTransactionsRequest
from ..responses.trust import ListTransactionsResponse
class TransactionsResource(FortressResource):
    """Custodial Accounts API"""
    def __init__(self):
        super().__init__("/api/trust/v1/transactions")

    def list(self, request:ListTransactionsRequest):
        """List all resources"""
        params = request.to_params()

        response = self.request(method="GET", url=self.base_url, params=params)
        return ListTransactionsResponse(response.json())

