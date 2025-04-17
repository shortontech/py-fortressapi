from fortress_api.api_model import ApiModel
from fortress_api.responses.trust.business_document_response import BusinessDocumentResponse
from .address_response import AddressResponse


class BusinessIdentityResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    """id of the tenant identity"""

    company_name = ApiModel.fields.char(required=False)
    """name of the tenant"""

    phone = ApiModel.fields.char(required=False)
    """phone number of the tenant"""

    ein = ApiModel.fields.char(required=False)
    """EIN of the tenant"""

    website = ApiModel.fields.char(required=False)
    """website of the tenant"""

    region_of_formation = ApiModel.fields.char(required=False)
    """region of formation of the tenant"""

    description = ApiModel.fields.char(required=False)
    """description of the tenant"""

    established_on = ApiModel.fields.date(required=False)
    """date the tenant was established"""

    legal_structure = ApiModel.fields.char(required=False)
    """legal structure of the tenant"""

    mailing_address = ApiModel.fields.child(related=AddressResponse, required=False)
    """mailing address of the tenant"""

    naics = ApiModel.fields.decimal(required=False)
    """NAICS code of the tenant"""

    naics_description = ApiModel.fields.char(required=False)
    """NAICS description of the tenant"""

    is_suspended = ApiModel.fields.bool(required=False)
    """whether the tenant is suspended"""

    identityContainerId = ApiModel.fields.char(required=False)
    """id of the identity container"""

    kycLevel = ApiModel.fields.char(required=False)
    """KYC level of the tenant"""

    type = ApiModel.fields.char(required=False)
    """type of the tenant"""

    address = ApiModel.fields.child(related=AddressResponse, required=False)
    """address of the tenant"""

    email = ApiModel.fields.char(required=False)
    """email of the tenant"""

    documents = ApiModel.fields.child(related=BusinessDocumentResponse, required=False)
    """verification documents of the tenant"""
