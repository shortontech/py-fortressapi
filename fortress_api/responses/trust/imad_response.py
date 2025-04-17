from fortress_api.api_model import ApiModel


class IMADResponse(ApiModel):
    cycle_date = ApiModel.fields.char(required=False)
    """Cycle date"""
    input_source = ApiModel.fields.char(required=False)
    """Input source"""
    input_sequence_number = ApiModel.fields.char(required=False)
    """Input sequence number"""
    raw = ApiModel.fields.char(required=False)
    """Raw IMAD"""
