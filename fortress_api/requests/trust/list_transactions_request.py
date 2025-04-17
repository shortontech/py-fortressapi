from ...api_model import ApiModel
from ...responses.trust.list_transactions_response import ListTransactionsResponse

class ListTransactionsRequest(ApiModel):
    identity_id = ApiModel.fields.char(required=False)
    custodial_account_id = ApiModel.fields.char(required=False)
    payment_id = ApiModel.fields.char(required=False)
    page = ApiModel.fields.decimal(required=False)
    page_size = ApiModel.fields.decimal(required=False)

    def to_params(self):
        """Converts the object to a request dictionary"""
        params = {}
        if self.identity_id is not None:
            params['ownerIdentityId'] = self.identity_id
        if self.custodial_account_id is not None:
            params['custodialAccountId'] = self.custodial_account_id
        if self.payment_id is not None:
            params['paymentId'] = self.payment_id

        params['page'] = self.page
        params['pageSize'] = self.page_size
        return params
