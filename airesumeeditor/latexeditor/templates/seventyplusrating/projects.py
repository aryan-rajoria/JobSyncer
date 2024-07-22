from typing import List


"""
%-----------PROJECTS-----------------
\section{\textbf{Personal Projects}}
\resumeSubHeadingListStart
    \resumeProject
      {Web Based Facial Authentication(Liveness Detection)} %Project Name
      {A website based facial authentication system, implemented using a Chrome Extension.} %Project Name, Location Name
      {} %Event Dates

      \resumeItemListStart
        \item {Facilitating users' logins to websites without having to remember their credentials}
        \item {Used Live detection techniques to create high order security.}
        \item {Technology Used: Python, Reactjs, Bootstrap.}
    \resumeItemListEnd
    \vspace{-2mm}
    
    \resumeProject
      {Realtime Chat App} %Project Name
      {A react based web application which allow users to chat in real time. } %Project Name, Location Name
      {} %Event Dates

      \resumeItemListStart
        \item {Used Firebase Authentication(SDK) to facilitate authentication \& Cloud Firestore to store data.}
        \item {Technology Used: Reactjs, Firebase, Bootstrap, HTML.}
    \resumeItemListEnd
    \vspace{-2mm}

    \resumeProject
      {Covid-19 Tracker} %Project Name
      {Daily and weekly updated statistics tracking the number of COVID-19 cases, recovered, and deaths.} %Project Name, Location Name
      {} %Event Dates

      \resumeItemListStart
        \item {Tracking world-wide cases using google maps and live API stats and datasets.}
        \item {Technology Used : JavaScript , CSS, HTML, API.
}
    \resumeItemListEnd
      
  \resumeSubHeadingListEnd
\vspace{-8.5mm}

"""

class Projects:
    section_name = "Personal Projects"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        self.start = """
        \section{\textbf{Projects}}
        \resumeSubHeadingListStart
        """
        self.end = """
          \resumeSubHeadingListEnd
          \vspace{-5.5mm}
        """
        self.section_start = "\resumeProject"
        self.next_line = "\n"
        self.feature_start = """
        \resumeItemListStart
        """
        self.space = "\vspace{-3.0mm}"
        self.section_end = """
        \resumeItemListEnd
        \vspace{-2.0mm}
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
        text += "{"+sections.get('project_name')+"}"+"{" + self.next_line
        text += "{"+sections.get('project_description')+"}" + self.next_line
        text += self.feature_start
        text += self.add_features(sections.get('features'))
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

def update(project_name, project_heading, project_description, project_features):
  project_features_listed = ""
  for feature in project_features:
      project_features_listed += " \\item {" + feature + "} \n"
  return """
    \resumeProject
      \newcommand{\project_name}{"""+ project_name +"""} %Project Name
      \newcommand{\project_heading}{"""+ project_heading +"""} %Project Name%Project Name, Location Name
      \newcommand{\project_description}{"""+ project_description +"""} 

      \\resumeItemListStart
        {project_features_latex}\
      \\resumeItemListEnd
  """
