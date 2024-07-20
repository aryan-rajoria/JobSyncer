# Consume all services generates the resume.
import requests

def send_to_embedding_service_and_save(data_type, value):
    data = {data_type: value}
    r = r.requests.post("https://localhost:9001/embed", data)
    if r.status == 200:
        print("Success /embed called with data")
    else:
        print(r)
    return r.data


def generate_resume_pdf():
    pass 