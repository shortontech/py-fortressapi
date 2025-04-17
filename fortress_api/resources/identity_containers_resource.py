import json
from .fortress_resource import FortressResource
from ..requests.trust import IdentityContainerRequest
from ..responses.trust import IdentityContainerResponse

class IdentityContainersResource(FortressResource):
    """Personal Identities API"""
    def __init__(self):
        super().__init__(endpoint="/api/trust/v1/identity-containers")

    def create(self, item: IdentityContainerRequest):
        """Creates a new IdentityContainer and PersonalIdentity"""
        data = item.to_request()
        response = self.request(method="POST", url=self.base_url, data=json.dumps(data))

        return IdentityContainerResponse(response.json())
