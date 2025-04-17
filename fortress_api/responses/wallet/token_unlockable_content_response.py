from fortress_api.api_model import ApiModel
from .token_unlockable_content_file_response import TokenUnlockableContentFileResponse


class TokenUnlockableContentResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    """Unlockable content unique identifier"""

    privateMessage = ApiModel.fields.char(required=False)
    """Private message"""

    tokenUnlockableContentFiles = ApiModel.fields.list(related=TokenUnlockableContentFileResponse, required=False)
    """List of unlockable content files"""
