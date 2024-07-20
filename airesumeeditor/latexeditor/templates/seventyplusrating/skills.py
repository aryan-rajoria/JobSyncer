from typing import List

class Skills:
    section_name = "Technical Skills and Interests"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        pass

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