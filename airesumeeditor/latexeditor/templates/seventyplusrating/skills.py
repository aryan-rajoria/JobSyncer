from typing import List

class Skills:
    section_name = "Technical Skills and Interests"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        self.start = """
        \section{\textbf{Technical Skills and Interests}}
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
        \vspace{-16pt}
        """
        self.print_text = ""
    
    def get_data(self, data):
        self.data = data
    
    def add_features(self, features):
        text = ""
        for i in features:
            text += "\item { \textbf {"+features.get("text")+"}"+self.next_line + "}"
        return text

    def add_section(self, sections):
        text = self.section_start + self.feature_start
        text += self.add_features(sections.get('features'))
        text += self.section_end
        return text

    def print_segment(self) -> List[str]:
        self.print_text = self.start
        self.print_text += self.add_section(self.data)
        self.print_text += self.end
        return self.print_text
    
    def get_fields(self) -> List[str]:
        pass

"""
%-----------Technical skills-----------------
\section{\textbf{Technical Skills and Interests}}
 \begin{itemize}[leftmargin=0.05in, label={}]
    \small{\item{
     \textbf{Languages}{: C/C++, Python, Javascript, HTML+CSS } \\
     \textbf{Libraries }{: C++ STL, Python Libraries, ReactJs }\\ 
     \textbf{Web Dev Tools}{: Nodejs, VScode, Git, Github } \\ 
     \textbf{Frameworks}{: ReactJs } \\
     \textbf{Cloud/Databases}{:MongoDb, Firebase, Relational Database(mySql) } \\  
     
     \textbf{Relevent Coursework}{: Data Structures \& Algorithms, Operating Systems, Object Oriented Programming, Database Management System, Software Engineering. } \\ 
     \textbf{Areas of Interest}{: Web Design and Development, Cloud Security.} \\
     \textbf{Soft Skills}{: Problem Solving, Self-learning, Presentation, Adaptability} \\
    }}
 \end{itemize}
 \vspace{-16pt}

"""