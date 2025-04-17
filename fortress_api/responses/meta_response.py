
from fortress_api.api_model import ApiModel


class MetaResponse(ApiModel):
    page_count: Optional[int]
    resource_count: Optional[int]

    def __init__(self, source: dict):
        self.page_count = source.get('pageCount', None)
        self.resource_count = source.get('resourceCount', None)

class test(ApiModel):
    def __init__(self, message):
        print(message)
