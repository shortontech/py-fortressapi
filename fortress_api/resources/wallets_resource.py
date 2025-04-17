from .fortress_resource import FortressResource
from ..responses.wallet.list_wallets_response import ListWalletsResponse
from ..requests import ListWalletsRequest

class WalletsResource(FortressResource):
    """Custodial Accounts API"""
    def __init__(self):
        super().__init__("/api/wallet/v1/wallets")
    def list(self, request:ListWalletsRequest):
        """List all resources"""
        params = request.to_params()

        response = self.request(method="GET", params=params)
        return ListWalletsResponse(response.json())

