from typing import Optional
from requests import Response
from requests.exceptions import JSONDecodeError
import json

class FortressResponseError(Exception):
    error_format = "At {method} request to URL {url}\nResponse with status '{code}' from Fortress API.\n\t{message}"

    def __init__(
            self,
            response: Response,
            request_kwargs: dict):
        self.error_code = response.status_code
        self.error_message = ""
        self.url = request_kwargs['url']
        self.method = request_kwargs['method']
        self.data = request_kwargs.get('data', None)

        request_kwargs = request_kwargs.copy()

        try:
            json_dict = response.json()
            self.errors = json_dict['errors']
            errorStrs = [(key + ': ' + '\n\t'.join(self.errors[key])) for key in json_dict['errors']]
            self.error_message = '\n'.join(errorStrs).strip("\r\n\t ")
        except JSONDecodeError:
            self.error_message = "Text Response: {response}".format(response=response.text)
            return

    def __str__(self):
        text = FortressResponseError.error_format.format(
            url=self.url,
            code=str(self.error_code),
            method=self.method,
            message=self.error_message
        )
        if self.data is not None:
            text += "\nRequest:\n" + json.dumps(self.data, indent=4, sort_keys=True)
        return text
