from fortress_api.api_model import ApiModel


class TokenFileResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    """File unique identifier"""

    type = ApiModel.fields.char(required=False)
    """required: value of 'main', 'creatorProfilePhoto', or 'coverArt'"""

    name = ApiModel.fields.char(required=False)
    """required: Token file name"""

    extension = ApiModel.fields.char(required=False)
    """Token file extension"""

    blob_file_id = ApiModel.fields.char(required=False)
    """required: Blob file unique identifier"""

    size = ApiModel.fields.decimal(required=False)
    """required File size"""

    duration = ApiModel.fields.char(required=False)
    """Audio/video file duration"""

    pages = ApiModel.fields.decimal(required=False)
    """Number PDF file pages"""

    resolution = ApiModel.fields.char(required=False)
    """File resolution"""

    updated_at = ApiModel.fields.datetime(required=False)
    """Time of file modified"""
