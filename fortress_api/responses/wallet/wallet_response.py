from fortress_api.api_model import ApiModel


class WalletResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    name = ApiModel.fields.char(required=False)
    identityId = ApiModel.fields.char(required=False)
