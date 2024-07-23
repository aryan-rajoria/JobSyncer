# Consume all services generates the resume.
import requests
import json

EMBEDDER_URL = "http://localhost:9001/"
HEADERS = {'Content-Type': 'application/json'}

def send_to_embedding_service_and_save(data_type, value):
    data = {data_type: value}
    r = r.requests.post("https://localhost:9001/embed", data)
    if r.status == 200:
        print("Success /embed called with data")
    else:
        print(r)
    return r.data

def jd_embeddings(job_descriptions):
    data = {"jd": job_descriptions}
    r = requests.post(EMBEDDER_URL+"jd", data=data, headers = HEADERS)
    return True

def generate_resume_pdf():
    pass 

def cv_embeddings(cv_array):
    payload = json.dumps(cv_array)
    response = requests.post(EMBEDDER_URL+"cv", data = payload, headers=HEADERS)
    print("cv_embeddings run:",response.reason, response.content)
