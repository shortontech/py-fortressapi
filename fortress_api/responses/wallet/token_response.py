from fortress_api.api_model import ApiModel
from .token_property_response import TokenPropertyResponse
from .token_file_response import TokenFileResponse
from .token_unlockable_content_response import TokenUnlockableContentResponse


class TokenResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    """Token unique identifier"""

    name = ApiModel.fields.char(required=False)
    """Token name"""

    status = ApiModel.fields.char(required=False)
    """draft minting minted failed"""

    blockchain = ApiModel.fields.char(required=False)
    """ethereum polygon solana"""

    tx_hash = ApiModel.fields.char(required=False)
    """Blockchain transaction hash"""

    project_name = ApiModel.fields.char(required=False)
    """Project name"""

    project_id = ApiModel.fields.char(required=False)
    """Project unique identifier"""

    project_number_of_tokens = ApiModel.fields.decimal(required=False)
    """Project copies amount"""

    description = ApiModel.fields.char(required=False)
    """Token description"""

    royalty_wallet_address = ApiModel.fields.char(required=False)
    """Royalty wallet address"""

    royalty_percentage = ApiModel.fields.decimal(required=False)
    """Royalty percentage"""

    number = ApiModel.fields.decimal(required=False)
    """Token number"""

    minting_wallet_address = ApiModel.fields.char(required=False)
    """Minting wallet address"""

    can_retry_mint = ApiModel.fields.bool(required=False)
    """A value indicating whether mint can be started again to retry failed tokens"""

    token_properties = ApiModel.fields.list(related=TokenPropertyResponse, required=False)
    """List of properties"""

    token_files = ApiModel.fields.list(related=TokenFileResponse, required=False)
    """List of files"""

    token_unlockable_content = ApiModel.fields.list(related=TokenUnlockableContentResponse, required=False)
    """Represents unlockable content response model"""

    created_by_author = ApiModel.fields.char(required=False)
    """Creator full name"""

    created_by_user_avatar_file_name = ApiModel.fields.char(required=False)
    """User avatar filename"""

    created_by_first_name = ApiModel.fields.char(required=False)
    """User first name who created the token"""

    created_by_last_name = ApiModel.fields.char(required=False)
    """User last name who created the token"""

    modified_by_first_name = ApiModel.fields.char(required=False)
    """User first name who modified the token"""

    modified_by_last_name = ApiModel.fields.char(required=False)
    """User last name who modified the token"""

    modified_by_user_avatar_file_name = ApiModel.fields.char(required=False)
    """Modified by User avatar file name"""

    created_at = ApiModel.fields.datetime(required=False)
    """Creation date"""

    updated_at = ApiModel.fields.datetime(required=False)
    """Modified date"""
