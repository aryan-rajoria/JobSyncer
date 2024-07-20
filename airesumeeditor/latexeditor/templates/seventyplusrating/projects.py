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
          %-----------PROJECTS-----------------
          \section{\textbf{Personal Projects}}
          \resumeSubHeadingListStart
          """
        self.end = """
            \resumeSubHeadingListEnd
            \vspace{-8.5mm}
          """
    def update(project_name, project_heading, project_description, project_features):
        project_features_latex = ""
        for feature in project_features:
            project_features_latex += " \\item {" + feature + "}\n"
        return """
          %-------------------------------------------
          \resumeProject
            \newcommand{\project_name}{"""+ project_name +"""} %Project Name
            \newcommand{\project_heading}{"""+ project_heading +"""} %Project Name%Project Name, Location Name
            \newcommand{\project_description}{"""+ project_description +"""} 
            {} %Event Dates

            \\resumeItemListStart
              {project_features_latex}\
            \\resumeItemListEnd
        """
    def get_fields(self) -> List[str]:
        pass

