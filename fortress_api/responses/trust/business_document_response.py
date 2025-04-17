from fortress_api.api_model import ApiModel


class BusinessDocumentResponse(ApiModel):
    id = ApiModel.fields.char(required=False)

    identity_id = ApiModel.fields.char(required=False)

    personal_document_type = ApiModel.fields.char(required=False)
    """Values of 'license', 'identification', or 'Card passport'"""

    business_document_type = ApiModel.fields.char(required=False)
    """values of 'other', 'proofOfAddress', 'proofOfCompanyFormation'"""

    document_reference_id = ApiModel.fields.char(required=False)

    document_uuid = ApiModel.fields.char(required=False)

    document_check_status = ApiModel.fields.char(required=False)
    """Values of 'pending', 'automaticReviewInProgress', 'manualReviewNeeded', 'accepted', 'rejected' ,'resubmit'"""

    isVerified = ApiModel.fields.bool(required=False)
