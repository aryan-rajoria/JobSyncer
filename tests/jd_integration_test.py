import requests

def send_jd_put(resume_file_path, url):
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
        response = requests.post(url, data=resume_file, headers=headers)
        print("test response: ", response)
        print("JD successfully uploaded!")
    # except FileNotFoundError:
    #     print(f"Error: Resume file not found at '{resume_file_path}'")
    # except requests.exceptions.RequestException as e:
    #     print(f"Error sending PUT request: {e}")


if __name__ == "__main__":
    resume_path = "./tests/jd.json"
    target_url = "http://127.0.0.1:9001/jd"

    send_jd_put(resume_path, target_url)