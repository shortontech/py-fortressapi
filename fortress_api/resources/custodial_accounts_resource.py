from typing import Optional
import json
from .fortress_resource import FortressResource
from ..responses.trust.custodial_account_response import CustodialAccountResponse
from ..responses.trust.wire_instructions_response import WireInstructionsResponse
from ..requests.trust.wire_simulated_request import WireSimulatedRequest
from ..fortress_response_error import FortressResponseError

class CustodialAccountsResource(FortressResource):
    """Custodial Accounts API"""
    sandbox_incoming_wire_url = "{base}/sandbox/{id}/start-incoming-wire"
    fiat_deposit_instructions_url = "{base}/{id}/fiat-deposit-instructions/{currency}"
    def __init__(self):
        super().__init__("/api/trust/v1/custodial-accounts")

    def list(self, owner_identity_id:Optional[str] = None, page:int = 0, page_size:int = 100):
        """List all resources"""
        params = {"Page": page, "PageSize": page_size}
        if owner_identity_id is not None:
            params["OwnerIdentityId"] = owner_identity_id

        response = self.request(params=params)
        obj = response.json()
        custodial_accounts = [CustodialAccountResponse(item) for item in obj.get('data', [])]

        return custodial_accounts

    def create(self, personal_identity_id, type="personal"):
        data = {'type': type, 'personalIdentityId': personal_identity_id}
        response = self.request(method="POST",data=json.dumps(data))
        return CustodialAccountResponse(response.json())

    def simulate_wire(self, wire_simulated: WireSimulatedRequest):
        url = CustodialAccountsResource.sandbox_incoming_wire_url.format(base=self.base_url, id=wire_simulated.custodial_account_id)

        try:
            self.request(method="POST", url=url, data=json.dumps(wire_simulated.to_request()))
        except FortressResponseError as e:
            if e.error_code == 404:
                return False

        return True
    def fiat_deposit_instructions(self, custodial_account: CustodialAccountResponse, currency: str):
        url = CustodialAccountsResource.fiat_deposit_instructions_url.format(base=self.base_url, id=custodial_account.id, currency=currency)
        response = self.request(url=url)
        response_obj = response.json()

        if 'wire' in response_obj:
            return WireInstructionsResponse(response_obj['wire'])
        return None
