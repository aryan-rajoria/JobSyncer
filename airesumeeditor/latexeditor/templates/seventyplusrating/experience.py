from typing import List
from templates import BaseTemplate

class Experience(BaseTemplate):
    section_name = "Experience"

    def __init__(self) -> None:
        # initialization of any segment creates an empty object
        # TODO: a potential design flaw as could create and print empty
        # objects
        pass

    def get_fields(self) -> List[str]:
        pass

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