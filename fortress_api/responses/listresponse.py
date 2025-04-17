from fortress_api.api_model import ApiModel

def listresponse(data_type: any):
    def setup(cls):
        cls.data: Optional[List[any]] = None
        cls.meta: Optional[data_type] = None
        cls = dataclass(cls)
        constructor = cls.__init__

        def __init__(self, source: dict):
            if 'data' in source:
                self.data = []
                for wallet in source.get('data'):
                    self.data.append(data_type(wallet))
            if 'meta' in source:
                self.meta = data_type(source['meta'])
            constructor(cls)
        cls.__init__ = __init__
        return cls
    return setup
