from faker import Faker
from typing import Optional
from faker_e164.providers import E164Provider
from ..responses.trust import IdentityContainerResponse, AddressResponse
from ..resources.custodial_accounts_resource import CustodialAccountsResource
from ..resources.personal_identities_resource import PersonalIdentitiesResource
from .address_factory import AddressFactory
from .identity_container_factory import IdentityContainerFactory

class CustodialAccountFactory:
    def make(self, fake:Optional[Faker] = None, address:Optional[AddressResponse] = None, identity_container:Optional[IdentityContainerResponse] = None):
        if fake is None:
            fake = Faker()
            fake.add_provider(E164Provider)

        if address is None:
            address = AddressFactory().make()

        if identity_container is None:
            identity_container = IdentityContainerFactory().make(address=address)

        acc = CustodialAccountsResource().create(personal_identity_id=identity_container.personal_identity)

        # verify the personal account attached to the custodial account.
        PersonalIdentitiesResource().upload_document(personal_identity_id=acc.owner_identity_id, document_type="license", document_front_path="state-id.jpg")
       return acc