from .fortress_resource import FortressResource
from ..responses.trust.list_payments_response import ListPaymentsResponse
from ..requests.trust.wire_simulated_request import WireSimulatedRequest
from ..requests.trust import ListPaymentsRequest
class PaymentsResource(FortressResource):
    """Custodial Accounts API"""
    def __init__(self):
        super().__init__("/api/trust/v1/payments")
    def list(self, request:ListPaymentsRequest):
        """List all resources"""
        params = request.to_params()

        response = self.request(method="GET", url=self.base_url, params=params)
        return ListPaymentsResponse(response.json())

