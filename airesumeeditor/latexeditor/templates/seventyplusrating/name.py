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

"""
%-------------------------------------------
%%%%%%  CV STARTS HERE  %%%%%%%%%%%
%%%%%% DEFINE ELEMENTS HERE %%%%%%%
\newcommand{\name}{Prashant Singh} % Your Name
\newcommand{\course}{Computer Science and Engineering} % Your Program
\newcommand{\roll}{xxxxxxx} % Your Roll No.
\newcommand{\phone}{xxxxxxxx} % Your Phone Number
\newcommand{\emaila}{prashantxxxxx@gmail.com} %Email 1

\begin{document}
\fontfamily{cmr}\selectfont
%----------HEADING-----------------

{
\begin{tabularx}{\linewidth}{L r} \\
  \textbf{\Large \name} & {\raisebox{0.0\height}{\footnotesize \faPhone}\ +91-\phone}\\
  {Roll No.: \roll } & \href{mailto:\emaila}{\raisebox{0.0\height}{\footnotesize \faEnvelope}\ {\emaila}} \\
  Bachelor of Technology & \href{https://github.com/xxxxx}{\raisebox{0.0\height}{\footnotesize \faGithub}\ {GitHub Profile}} \\  
  {Shri Ramdeobaba College of Engineering and Management, Nagpur} & \href{www.linkedin.com/in/xxxx/}{\raisebox{0.0\height}{\footnotesize \faLinkedin}\ {LinkedIn Profile}}
\end{tabularx}
}
"""