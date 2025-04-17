from typing import Any, List, Optional


class InvalidValueError(Exception):
    pass


class HasToDict:
    def to_dict() -> Optional[dict]:
        return None


class ResponseField:
    def __init__(
        self,
        type: Optional[str] = None,
        required: Optional[bool] = None
    ) -> None:
        self.required = required if required is not None else required
        self.type = type
        pass

    def valid(self, val: any) -> bool:
        """Indicates if a value is valid"""
        return not self.required or val is not None

    def getDefaultValue(self) -> any:
        """Returns the default value, which is by default, None."""
        val: any = None
        return val

    def validate(self, val: any):
        """
        Checks the value to see if it's valid.
        """
        if self.required and val is None:
            raise InvalidValueError("Invalud value %s" % str(val))


class CharField(ResponseField):
    pass


class DecimalField(ResponseField):
    pass


class UuidField(ResponseField):
    pass


class DateField(ResponseField):
    pass


class BoolField(ResponseField):
    pass

class DateTimeField(ResponseField):
    pass

class FileField(ResponseField):
    pass

class ListField(ResponseField):
    def __init__(
        self,
        related: any,
        type: Optional[str] = None,
        required: Optional[bool] = None
    ) -> None:
        self.related = related
        super().__init__(type=type, required=required)

    def getDefaultValue(self) -> any:
        """Initializes an empty list"""
        val: List[self.related] = list()
        return val


class ChildModelField(ResponseField, HasToDict):
    def __init__(
        self,
        related: any,
        type: Optional[str] = None,
        required: Optional[bool] = None
    ) -> None:
        super().__init__(type=type, required=required)
        self.related = related
        pass
    pass

    def getDefaultValue(self) -> any:
        val: self.related = self.related()
        return val


class ApiModel(HasToDict):
    TYPE_HEADER = "HEADER"

    class fields:
        @classmethod
        def uuid(cls, type: Optional[str] = None, required: bool = True):
            return CharField(type=type, required=required)

        @classmethod
        def char(cls, type: Optional[str] = None, required: bool = True):
            return UuidField(type=type, required=required)

        @classmethod
        def bool(cls, required: bool = True):
            return UuidField(type=None, required=required)

        @classmethod
        def decimal(cls, required: bool = True):
            return DecimalField(type=None, required=required)

        @classmethod
        def date(cls, required: bool = True):
            return DateField(type=None, required=required)

        @classmethod
        def datetime(cls, required: bool = True):
            return DateTimeField(type=None, required=required)

        @classmethod
        def file(cls, required: bool = True):
            return FileField(type=None, required=required)

        @classmethod
        def list(
            cls,
            related: any,
            type: Optional[str] = None,
            required: bool = True
        ):
            return ListField(
                related=related,
                type=type,
                required=required
            )

        @classmethod
        def child(
            cls,
            related: any,
            type: Optional[str] = None,
            required=True
        ):
            return ChildModelField(
                related=related,
                type=type,
                required=required
            )

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Validates properties when setting them.
        """
        if hasattr(self.__class__, __name):
            field = getattr(self.__class__, __name)
            if isinstance(field, ResponseField):
                field.validate(__value)
                super().__setattr__(__name, __value)

    def __init__(self, values: Optional[dict] = None, **kwargs) -> None:
        """Sets default values on this instance"""
        for property, field in vars(self.__class__).items():
            if isinstance(field, ResponseField):
                if property in kwargs.keys():
                    setattr(self, property, kwargs.get(property))
                elif isinstance(values, dict) and property in values.keys():
                    setattr(self, property, values.get(property))
                else:
                    setattr(self, property, field.getDefaultValue())

    def to_dict(self) -> Optional[dict]:
        """Converts the response model to a dict"""
        result: dict = dict()
        is_empty: bool = True

        # Check to see if all field values are null.
        for property, field in vars(self.__class__).items():
            if isinstance(field, ResponseField):
                currVal = getattr(self, property)
                if currVal is not None:
                    is_empty = False

        # When there's nothing to return, return nothing.
        if is_empty:
            return None

        # Handle sub-models
        for property, field in vars(self.__class__).items():
            if isinstance(field, ResponseField):
                currVal = getattr(self, property)
                if isinstance(currVal, HasToDict):
                    currVal: any = currVal.to_dict()

                if currVal is not None or field.required:
                    result[property] = currVal

        return result

    @classmethod
    def get_response_instance(cls) -> Optional[any]:
        return ApiModel()

    @classmethod
    def get_path(cls) -> Optional[str]:
        return None

    def get_method(self) -> Optional[str]:
        if (hasattr(self, 'method')):
            return self.method

    def submit(self) -> any:
        return None
