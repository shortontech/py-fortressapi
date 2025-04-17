from fortress_api.api_model import ApiModel
from fortress_api.responses.trust.address_response import AddressResponse
from .personal_document_response import PersonalDocumentResponse


class PersonalIdentityResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    first_name = ApiModel.fields.char(required=False)
    last_name = ApiModel.fields.char(required=False)
    middle_name = ApiModel.fields.char(required=False)
    date_of_birth = ApiModel.fields.date(required=False)
    phone = ApiModel.fields.char(required=False)
    ssn = ApiModel.fields.char(required=False)
    is_suspended = ApiModel.fields.char(required=False)
    full_name = ApiModel.fields.char(required=False)
    identity_container_id = ApiModel.fields.char(required=False)
    kyc_level = ApiModel.fields.char(required=False)
    type = ApiModel.fields.char(required=False)
    address = ApiModel.fields.char(related=AddressResponse, required=False)
    email = ApiModel.fields.char(required=False)
    documents = ApiModel.fields.list(related=PersonalDocumentResponse, required=False)
