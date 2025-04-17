from fortress_api.api_model import ApiModel


class CustodialAccountResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    "id of the custodial account"

    owner_identity_id = ApiModel.fields.char(required=False)
    "id of the identity that owns the custodial account"

    account_status = ApiModel.fields.char(required=False)
    "status of the custodial account"

    account_type = ApiModel.fields.char(required=False)
    "type of the custodial account"

    account_number = ApiModel.fields.char(required=False)
    "account number of the custodial account"
