from typing import List

class Name:
    section_name = "Name Section"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        pass

    def get_fields(self) -> List[str]:
        pass

def update(name, course, phone, email, roll_number, github_link, linkedin_link):

    return """
    %-------------------------------------------
    %%%%%%  CV STARTS HERE  %%%%%%%%%%%
    %%%%%% DEFINE ELEMENTS HERE %%%%%%%
    \newcommand{\name}{"""+ name +"""} % Your Name
    \newcommand{\course}{"""+ course +"""} % Your Program
    \newcommand{\roll}{"""+ roll_number +"""} % Your Roll No.
    \newcommand{\phone}{"""+phone+"""} % Your Phone Number
    \newcommand{\emaila}{"""+email+"""} % Email 1

    \begin{document}
    \fontfamily{cmr}\selectfont
    %----------HEADING-----------------

    {
    \begin{tabularx}{\linewidth}{L r} \\
    \textbf{\Large \name} & {\raisebox{0.0\height}{\footnotesize \faPhone}\ +91-\phone}\\
    {Roll No.: \roll } & \href{mailto:\emaila}{\raisebox{0.0\height}{\footnotesize \faEnvelope}\ {\emaila}} \\
    Bachelor of Technology & \href{"""+ github_link +"""}{\raisebox{0.0\height}{\footnotesize \faGithub}\ {GitHub Profile}} \\  
    {Shri Ramdeobaba College of Engineering and Management, Nagpur} & \href{"""+linkedin_link+"""}{\raisebox{0.0\height}{\footnotesize \faLinkedin}\ {LinkedIn Profile}}
    \end{tabularx}
    }
    """