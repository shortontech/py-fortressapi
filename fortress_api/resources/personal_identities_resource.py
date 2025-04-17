from .fortress_resource import FortressResource
from ..fortress_client import FortressClient
from ..responses.trust.personal_identity_response import PersonalIdentityResponse
from ..responses.trust.personal_document_response import PersonalDocumentResponse

class PersonalIdentitiesResource(FortressResource):
    by_id_url = "{base}/{id}"
    upload_document_url = "{base}/{id}/documents"
    upgrade_url = "{base}/{id}/upgrade"
    """Personal Identities API"""
    def __init__(self):
        super().__init__(endpoint="/api/trust/v1/personal-identities")

    def upgrade(self, personal_identity_id: str):
        """Upgrades KYC of a personal identity"""
        url = PersonalIdentitiesResource.upgrade_url.format(base=self.base_url, id=personal_identity_id)
        response = self.request(method="POST", url=url)
        return PersonalIdentityResponse(response.json())

    def get(self, personal_identity_id: str):
        """Upgrades KYC of a personal identity"""
        response = self.request(url=PersonalIdentitiesResource.by_id_url.format(base=self.base_url, id=personal_identity_id))
        return PersonalIdentityResponse(response.json())


    def upload_document(
        self,
        personal_identity_id: str,
        document_type: str,
        document_front_path: str
    ):
        """Uploads a document to a personal identity for the purposes of KYC"""
        url = PersonalIdentitiesResource.upload_document_url.format(base=self.base_url, id=personal_identity_id)
        short_name = document_front_path.split("/")[-1]
        data = {'DocumentType': document_type}

        files = [
            ('DocumentFront',(short_name, open(document_front_path,'rb'),'image/jpeg'))
        ]

        response = self.request(method="POST", url=url, headers=FortressClient.get_headers, data=data, files=files)
       return PersonalDocumentResponse(response.json())