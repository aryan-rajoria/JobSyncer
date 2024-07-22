from typing import List

# %-------------------------
# % Custom commands
# \newcommand{\resumeItem}[1]{
#   \item\small{
#     {#1 \vspace{-2pt}}
#   }
# }

# \newcommand{\resumeSubheading}[4]{
#   \vspace{-2pt}\item
#     \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
#       \textbf{#1} & #2 \\
#       \textit{\small#3} & \textit{\small #4} \\
#     \end{tabular*}\vspace{-7pt}
# }

# \newcommand{\resumeSubSubheading}[2]{
#     \item
#     \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
#       \textit{\small#1} & \textit{\small #2} \\
#     \end{tabular*}\vspace{-7pt}
# }

# \newcommand{\resumeProjectHeading}[2]{
#     \item
#     \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
#       \small#1 & #2 \\
#     \end{tabular*}\vspace{-7pt}
# }

# \newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

# \renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

# \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
# \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
# \newcommand{\resumeItemListStart}{\begin{itemize}}
# \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

# %-------------------------------------------

class Education:
    section_name = "Education"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        self.start = """
        \section{\textbf{Education}}
        \resumeSubHeadingListStart
        """
        self.end = """
          \resumeSubHeadingListEnd
          \vspace{-5.5mm}
        """
        self.section_start = "\resumeSubheading"
        self.next_line = "\n"
        self.section_end = """
        \resumeItemListEnd
    
        \vspace{-3.0mm}
        """
        self.print_text = ""
    
    def get_data(self, data):
        self.data = data

    def add_section(self, sections):
        text = self.section_start + self.next_line
        text += "{"+sections.get('degree')+"}"+"{"+ sections.get('cgpa') +"}" + self.next_line
        text += "{"+sections.get('institution')+"}"+"{"+ sections.get('duration') +"}" + self.next_line
        text += self.section_end
        return text

    def print_segment(self) -> List[str]:
        self.print_text = self.start
        # print each section
        for i in self.data:
            self.print_text += self.add_section(i)
        self.print_text += self.end
        return self.print_text

    def get_fields(self) -> List[str]:
        pass

def update(degree, cgpa, institution, duration):
    return """
    %-----------EDUCATION-----------
    \section{\textbf{Education}}
      \resumeSubHeadingListStart
        \resumeSubheading
          {""" + degree + """}{CGPA: """ + cgpa + """}
          {""" + institution + """}{ """ + duration + """}
      \resumeSubHeadingListEnd
    \vspace{-5.5mm}
    %
    """

# """
# %-----------EDUCATION-----------
# \section{\textbf{Education}}
#   \resumeSubHeadingListStart
#     \resumeSubheading
#       {Bachelor of Technology in Computer Science and Engineering(Cyber Security)}{CGPA: xx}
#       {Shri Ramdeobaba College of Engineering and Management, Nagpur}{2020-24}
#   \resumeSubHeadingListEnd
# \vspace{-5.5mm}
# %
# """