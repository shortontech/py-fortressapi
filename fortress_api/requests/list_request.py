from fortress_api.api_model import ApiModel
from .. responses.listresponse import ListResponse


class ListRequest(ApiModel):
    page = ApiModel.fields.decimal(required=False)

    def __init__(self):
        self.page = 1
        self.pageSize = 50

    def get_path(self) -> str:
        return self.path

    def set_path(self, path: str):
        self.path = path
        return self

    def get_response_instance(self):
        return ListResponse()

    def get_method(self) -> str:
        return 'GET'
