from typing import List

class Education:
    section_name = "Education"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        pass

    def get_fields(self) -> List[str]:
        pass

"""
%-----------EDUCATION-----------
\section{\textbf{Education}}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Bachelor of Technology in Computer Science and Engineering(Cyber Security)}{CGPA: xx}
      {Shri Ramdeobaba College of Engineering and Management, Nagpur}{2020-24}
  \resumeSubHeadingListEnd
\vspace{-5.5mm}
%
"""