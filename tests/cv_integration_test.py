import requests
import json

def send_resume_put(resume_file_path, url):
    """Sends a PUT request with a resume JSON file to the specified URL.

    Args:
        resume_file_path (str): The path to the resume.json file.
        url (str): The URL to which the resume should be sent.
    """

    # try:
    with open(resume_file_path, 'r') as resume_file:
        headers = {
            'Content-Type': 'application/json'
        }
        resume = json.dumps(json.loads(resume_file.read()).get('cv', None))
        response = requests.post(url, data=resume, headers=headers)
        print("test response: ", response)
        print("Resume successfully uploaded!")
    # except FileNotFoundError:
    #     print(f"Error: Resume file not found at '{resume_file_path}'")
    # except requests.exceptions.RequestException as e:
    #     print(f"Error sending PUT request: {e}")


if __name__ == "__main__":
    resume_path = "./tests/resume.json"
    target_url = "http://127.0.0.1:9001/cv"

    send_resume_put(resume_path, target_url)