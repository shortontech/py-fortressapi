from faker import Faker
from typing import Optional
from datetime import date
from ..responses.trust import AddressResponse
from ..requests.trust import IdentityContainerRequest
from ..resources import IdentityContainersResource
from ..factories import address_factory
class IdentityContainerFactory:
    def make(self, fake:Optional[Faker] = None, address:Optional[AddressResponse] = None):

        if fake is None:
            from faker_e164.providers import E164Provider
            fake = Faker()
            fake.add_provider(E164Provider)

        if address is None:
            address = address_factory().make()

        containers = IdentityContainersResource()
        result = IdentityContainerRequest()
        result.first_name = fake.first_name()
        result.last_name = fake.last_name()
        result.middle_name = fake.first_name()
        result.phone = fake.e164(region_code="US", valid=True, possible=True)
        result.ssn = fake.ssn()
        result.email = fake.email()
        result.date_of_birth = date.fromisoformat(fake.date_of_birth(minimum_age=21,maximum_age=95).strftime("%Y-%m-%d"))
        result.address = address

        # update the container with new data from the API.
       return containers.create(result)