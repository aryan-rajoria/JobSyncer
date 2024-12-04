from typing import List

class Responsibilities:
    section_name = "Positions of Responsibilities"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        self.start = """
        \section{\textbf{Positions of Responsibility}}
        \vspace{-0.4mm}
        \resumeSubHeadingListStart
        """
        self.end = """
          \resumeSubHeadingListEnd
        """
        self.section_start = "\resumePOR"
        self.next_line = "\n"
        self.feature_start = """
        \resumeItemListStart
        """
        self.section_end = """
        \resumeItemListEnd
        \vspace{-5.0mm}
        """
        self.print_text = ""
    
    def get_data(self, data):
        self.data = data
    
    def add_features(self, features):
        text = ""
        for i in features:
            text += "\item {"+features.get("text")+"}"+self.next_line
        return text

    def add_section(self, sections):
        text = self.section_start + self.next_line
        text += "{"+sections.get('position')+"}"+"{" + self.next_line
        text += "{"+sections.get('organization')+"}"+"{" + self.next_line
        text += "{"+sections.get('tenure')+"}"+"{" + self.next_line
        text += self.feature_start
        text += self.add_features(sections.get('features'))
        text += self.section_end
        return text

    def print_segment(self) -> List[str]:
        self.print_text = self.start
        for i in self.data:
            self.print_text += self.add_section(i)
        self.print_text += self.end
        return self.print_text

    def get_fields(self) -> List[str]:
        pass
"""

%-----------Positions of Responsibility-----------------
\section{\textbf{Positions of Responsibility}}
\vspace{-0.4mm}
\resumeSubHeadingListStart
\resumePOR{On Desk Registrations Volunteer } % Position
    {Aarhant Cyber Week Event - RCOEM, Nagpur} %Club,Event
    {Oct - Dec 2022} %Tenure Period \\
    \resumeItemListStart
    \item {Helped to attract close to 300 attendees to the event.}
    \item {Collected over Rs. 20,000 in entry fees for different activities.}
    \resumeItemListEnd

\resumeSubHeadingListEnd
\vspace{-5mm}

"""