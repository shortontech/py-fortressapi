from fortress_api.api_model import ApiModel


class PersonalDocumentResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    "id of the personal document"

    identityId = ApiModel.fields.char(required=False)
    "id of the identity that owns the personal document"

    personalDocumentType = ApiModel.fields.char(required=False)
    "type"

    documentReferenceId = ApiModel.fields.char(required=False)
    "document reference id"

    documentUuid = ApiModel.fields.char(required=False)
    "document id"

    documentCheckStatus = ApiModel.fields.bool(required=False)
    "document check status"

    isVerified = ApiModel.fields.bool(required=False)
    "verification status of the document"
