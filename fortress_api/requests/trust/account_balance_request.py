from fortress_api.api_model import ApiModel


class AccountBalanceRequest(ApiModel):
    custodialAccountId = ApiModel.fields.char(required=False)

    def get_path(self):
        return f'/api/trust/v1/custodial-accounts/{self.custodial_account_id}/balances'

    def get_method(self):
        return 'GET'
