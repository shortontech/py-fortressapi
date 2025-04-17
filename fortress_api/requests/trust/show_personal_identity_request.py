from fortress_api.api_model import ApiModel


class ShowPersonalIdentityRequest(ApiModel):
    identityId = ApiModel.fields.char(required=False)
