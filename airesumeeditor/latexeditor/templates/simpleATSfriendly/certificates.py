from typing import List
from templates import BaseTemplate

class Certificates(BaseTemplate):
    section_name = "Online Courses & Certifications"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        super().__init__()
    
    def get_fields(self) -> List[str]:
        pass