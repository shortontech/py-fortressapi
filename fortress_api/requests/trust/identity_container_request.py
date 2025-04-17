from fortress_api.api_model import ApiModel
from .address_request import AddressRequest
from datetime import date


class IdentityContainerRequest(ApiModel):
    id = ApiModel.fields.char(required=False)
    email = ApiModel.fields.char(required=False)
    first_name = ApiModel.fields.char(required=False)
    middle_name = ApiModel.fields.char(required=False)
    last_name = ApiModel.fields.char(required=False)
    phone = ApiModel.fields.char(required=False)
    date_of_birth = ApiModel.fields.date(required=False)
    ssn = ApiModel.fields.char(required=False)
    address = ApiModel.fields.child(related=AddressRequest, required=False)

    def to_request(self):
        result = {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "phone": self.phone,
            "ssn": self.ssn,
            "email": self.email,
        }
        if self.date_of_birth is not None:
            result["dateOfBirth"] = self.date_of_birth.strftime('%Y-%m-%d')

        if self.middle_name is not None:
            result['middleName'] = self.middle_name

        if self.address is not None:
            result['address'] = self.address.to_request()
        return result
