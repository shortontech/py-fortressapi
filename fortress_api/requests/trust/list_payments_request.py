from fortress_api.api_model import ApiModel

class ListPaymentsRequest(ApiModel):
    ownerIdentityId = ApiModel.fields.char(required=False)
    page = ApiModel.fields.decimal(required=False)
    pageSize = ApiModel.fields.decimal(required=False)
