import requests
from jd_integration_test import send_jd_put as jd_send
from tests.cv_integration_test import send_resume_put as cv_send

if __name__=="__main__":

    resume_path = "./tests/jd.json"
    target_url = "http://127.0.0.1:9001/jd"
    jd_send(resume_path, target_url)
    
    resume_path = "./tests/resume.json"
    target_url = "http://127.0.0.1:9001/cv"
    cv_send(resume_path, target_url)


    target_url = "http://127.0.0.1:9001/resume_layout"
    r = requests.get(target_url)
    print("test response:", r)
    print("Resume generated")

