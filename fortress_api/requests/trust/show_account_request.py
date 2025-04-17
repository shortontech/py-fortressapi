from fortress_api.api_model import ApiModel


class ShowAccountRequest(ApiModel):
    custodialAccountId = ApiModel.fields.char(required=False)
