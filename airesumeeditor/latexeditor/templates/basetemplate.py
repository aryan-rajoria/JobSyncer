class BaseTemplate:
    def __init_subclass__(cls) -> None:
        if not hasattr(cls, 'section_name'):
            raise TypeError(f"{cls.__name__} must define a class variable called `section_name`.")
        if not callable(getattr(cls, 'get_fields', None)):
            raise TypeError(f"{cls.__name__} must have method `get_fields`.")