from fortress_api.api_model import ApiModel


class TokenPropertyResponse(ApiModel):
    id = ApiModel.fields.char(required=False)
    """Property unique identifier"""

    type = ApiModel.fields.char(required=False)
    """Value of 'property', 'ranking', 'numericTrait' 'dateTrait'"""

    trait_type_key = ApiModel.fields.char(required=False)
    """Trait type key"""

    date_trait = ApiModel.fields.date(required=False)
    """Date trait"""

    numeric_trait_type = ApiModel.fields.char(required=False)
    """If it's set, value of 'number' 'boostNumber' 'boostPercentage' 'maxValue'"""

    numericTraitValue = ApiModel.fields.decimal(required=False)
    """Value of numeric trait"""

    stringValue = ApiModel.fields.char(required=False)
    """Value of property"""
