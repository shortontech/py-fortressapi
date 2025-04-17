from fortress_api.api_model import ApiModel


class ListWalletsRequest(ApiModel):
    page = ApiModel.fields.decimal(required=False)
    page_size = ApiModel.fields.decimal(required=False)

    def to_params(self):
        """Converts the object to a request dictionary"""
        params = {
            'page': self.page,
            'pageSize': min(self.page_size, 50)
        }
        return params
