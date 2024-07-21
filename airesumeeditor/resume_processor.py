import json
from service_helper import send_to_embedding_service_and_save, jd_embeddings

class ResumeProcessor:

    def __init__(self):
        pass
    
    def cv(self):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        
        # assume json
        segments = json.segments()

        for segment in json_data:
            title= segment['segment_title']
            match title:
                case "proj":
                    pass
                case "education":
                    pass
                case "experience":
                    pass
                case "name":
                    pass
                case "projects":
                    pass
                case "responsibilities":
                    pass
                case "skills":
                    pass

    def jd(self, job_description):
        embedding = jd_embeddings(job_description)
        print(embedding)

    def generate_resume_text():
        pass