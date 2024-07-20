from typing import List
from templates import BaseTemplate

class Education(BaseTemplate):
    section_name = "Education"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        pass

    def get_fields(self) -> List[str]:
        pass