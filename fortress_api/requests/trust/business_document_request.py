from io import FileIO
from typing import List, Optional
import magic
from fortress_api.api_model import ApiModel

class BusinessDocumentRequest(ApiModel):
    DocumentType = ApiModel.fields.file(required=False)
    """value of 'proofOfAddress', 'proofOfCompanyFormation', 'other'"""
    DocumentFront = ApiModel.fields.file(required=False)
    """An image of the front of the ID. For passports, the front is the page containing the user's name and photograph."""

    DocumentBack = ApiModel.fields.file(required=False)
    """An image of the back of the ID. This parameter is optional, but recommended for drivers licenses."""

    SelfPortrait = ApiModel.fields.file(required=False)
    """A self-portrait of the user for facial recognition. This parameter is optional and can be used as an additional data point for verification."""

    def to_request(self):
        result = {}
        result['DocumentType'] = self.DocumentType
        return result

    def to_files(self):
        files: List[tuple] = []

        def add_file(var_name: str, file: Optional[FileIO]):
            if file is not None:
                file_name: str = str(file.name).split('/')[-1]
                mime_type: str = magic.from_file(file.name)
                files.append((var_name, (file_name, file, mime_type)))

        add_file('DocumentFront', self.document_front)
        add_file('DocumentBack', self.document_back)
        add_file('SelfPortrait', self.self_portrait)
        return files
