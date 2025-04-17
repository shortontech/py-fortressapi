from requests import request, Response
from ..fortress_client import FortressClient
from ..fortress_response_error import FortressResponseError
class FortressResource:
    """Base API resource"""
    base_url: str

    def __init__(self, endpoint: str):
        FortressClient.login()
        self.base_url = FortressClient.settings.FORTRESS_BASE_URL + endpoint


    def check_response(self, response: Response, request_kwargs:dict):
        """Check the response from a request"""
        if response.status_code in [200, 201, 202]:
            return
        raise FortressResponseError(response, request_kwargs)

    def request(self, **kwargs):
        """Send a request, wrapper for requests.request"""
        if 'method' not in kwargs:
            kwargs['method'] = 'POST' if 'data' in kwargs else 'GET'


        if 'headers' not in kwargs:
            kwargs['headers'] = FortressClient.post_headers if kwargs['method'] in ['POST', 'PUT', 'PATCH'] else FortressClient.get_headers

        if 'url' not in kwargs:
            kwargs['url'] = self.base_url

        response = request(**kwargs)


        self.check_response(response, kwargs)
       return response