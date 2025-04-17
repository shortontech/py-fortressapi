from fortress_api.api_model import ApiModel
from .personal_identity_response import PersonalIdentityResponse
from ..listresponse import listresponse

@listresponse(PersonalIdentityResponse)
class ListPersonalIdentitiesResponse(ApiModel):
    pass
