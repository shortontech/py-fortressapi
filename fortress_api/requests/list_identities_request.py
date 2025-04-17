from .list_request import ListRequest
class ListIdentitiesRequest(ListRequest):

    def get_path(self) -> str:
        return '/api/compliance/v1/identities'
