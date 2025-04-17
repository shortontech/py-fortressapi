from fortress_api.api_model import ApiModel
from .address_response import AddressResponse


class IdentityContainerResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    """id of the identity container"""

    email = ApiModel.fields.char(required=False)
    """email of the related personal identity"""

    first_name = ApiModel.fields.char(required=False)
    """first name of the related personal identity"""

    middle_name = ApiModel.fields.char(required=False)
    """middle name of the related personal identity"""

    last_name = ApiModel.fields.char(required=False)
    """last name of the related personal identity"""

    phone = ApiModel.fields.char(required=False)
    """phone of the related personal identity"""

    personal_identity = ApiModel.fields.char(required=False)
    """personal identity id of the identity container"""

    date_of_birth = ApiModel.fields.date(required=False)
    """date of birth of the identity container"""

    ssn = ApiModel.fields.char(required=False)
    """ssn of the identity container"""

    is_suspended = ApiModel.fields.char(required=False)
    """whether the personal identity is suspended"""

    business_identities = ApiModel.fields.list(related=str, required=False)
    """tenant identities of the identity container"""

    address = ApiModel.fields.child(related=AddressResponse, required=False)
    """address of the personal identity"""
