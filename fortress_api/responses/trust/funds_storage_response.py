
from fortress_api.api_model import ApiModel
from .wire_originator_response import WireOriginatorResponse
from .imad_response import IMADResponse


class FundsStorageResponse(ApiModel):
    identity_id = ApiModel.fields.char(required=False)
    """Identity identifier"""

    custodial_account_id = ApiModel.fields.char(required=False)
    """Custodial account identifier"""

    external_account_id = ApiModel.fields.char(required=False)
    """External account identifier"""

    incoming_transfer_origin = ApiModel.fields.char(required=False)
    """Incoming transfer origin"""

    crypto_address = ApiModel.fields.char(required=False)
    """Crypto address"""

    comment = ApiModel.fields.char(required=False)
    """Originator to beneficiary info"""

    originator = ApiModel.fields.char(related=WireOriginatorResponse, required=False)
    """Originator of the wire"""
    imad = ApiModel.fields.child(related=IMADResponse, required=False)
    """IMAD of the wire"""

    def __init__(self, source: dict):
        self.identity_id = source.get('identityId', None)
        self.custodial_account_id = source.get('custodialAccountId', None)
        self.external_account_id = source.get('externalAccountId', None)
        self.incoming_transfer_origin = source.get('incomingTransferOrigin', None)
        self.crypto_address = source.get('cryptoAddress', None)
        self.comment = source.get('comment', None)
        self.originator = WireOriginatorResponse(source['originator']) if 'originator' in source else None
        self.imad = IMADResponse(source['imad']) if 'imad' in source else None
