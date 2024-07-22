import json
from airesumeeditor.service_helper import cv_embeddings, jd_embeddings

class ResumeProcessor:

    def __init__(self):
        pass
    
    def cv(self, json_data):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        
        # assume json
        cv_array = json_data
        cv_embeddings(cv_array)

    def jd(self, job_description):
        embedding = jd_embeddings(job_description)
        print(embedding)

    def generate_resume_text():
        pass