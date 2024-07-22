from typing import List
from templates import BaseTemplate

class Experience(BaseTemplate):
    section_name = "Experience"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        self.start = """
        \section{\textbf{Experience}}
        \resumeSubHeadingListStart
        """
        self.end = """
          \resumeSubHeadingListEnd
          \vspace{-5.5mm}
        """
        self.section_start = "\resumeSubheading"
        self.next_line = "\n"
        self.feature_start = """
        \vspace{-2.0mm}
        \resumeItemListStart
        """
        self.space = "\vspace{-3.0mm}"
        self.section_end = """
        \resumeItemListEnd
    
        \vspace{-3.0mm}
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
        text += "{"+sections.get('title')+"}"+"{"+ sections.get('location') +"}" + self.next_line
        text += "{"+sections.get('company')+"}"+"{"+ sections.get('date') +"}" + self.next_line
        text += self.feature_start
        # print each features
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
    
        

"""

%-----------EXPERIENCE-----------------
\section{\textbf{Experience}}
  \resumeSubHeadingListStart
    \resumeSubheading
      {AWS Cloud Virtual Internship}{Online}
      {AICTE-Eduskills}{May - July 2023}
      \vspace{-2.0mm}
      \resumeItemListStart
    \item {In-depth understanding of AWS cloud computing services, including EC2, S3, RDS, Lambda, IAM, VPC, and more.}
    \item {Proficient in designing, deploying, and managing fault-tolerant, highly available, and scalable AWS solutions.}
    \item {Strong knowledge of architectural best practices, such as AWS Well-Architected Framework, security, performance, and cost optimization.}
    \item {Hands-on experience in cloud infrastructure provisioning, monitoring, and automation using AWS Management Console and AWS CLI.}
    \resumeItemListEnd
    
    \vspace{-3.0mm}
    
    \resumeSubheading
      {Palo Alto Cybersecurity Virtual Internship}{Online}
      {AICTE-Eduskills}{Dec 2022 - Feb 2023}
      \vspace{-2.0mm}
      \resumeItemListStart
    \item {Learned the fundamentals of Security Operations Center (SOC).}
    \item {Learned basics of Network \& Cloud Security.}
    \resumeItemListEnd
    
    \vspace{-3.0mm}
      
  \resumeSubHeadingListEnd
\vspace{-5.5mm}


"""