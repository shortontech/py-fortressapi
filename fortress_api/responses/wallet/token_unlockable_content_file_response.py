from fortress_api.api_model import ApiModel


class TokenUnlockableContentFileResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    """File unique identifier"""

    name = ApiModel.fields.char(required=False)
    """Token file name"""

    extension = ApiModel.fields.char(required=False)
    """Token file extension"""

    blobFileId = ApiModel.fields.char(required=False)
    """Blob file unique identifier"""

    size = ApiModel.fields.decimal(required=False)
    """File size"""

    duration = ApiModel.fields.char(required=False)
    """Audio/video file duration"""

    pages = ApiModel.fields.decimal(required=False)
    """Number PDF file pages"""

    resolution = ApiModel.fields.char(required=False)
    """File resolution"""

    title = ApiModel.fields.char(required=False)
    """Title"""

    description = ApiModel.fields.char(required=False)
    """Description"""

    updatedAt = ApiModel.fields.datetime(required=False)
    """Time of file modified"""

    createdBy = ApiModel.fields.char(required=False)
    """File creator"""
