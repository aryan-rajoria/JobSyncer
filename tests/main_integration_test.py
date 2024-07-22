import requests

def send_resume_put(resume_file_path, url):
    """Sends a PUT request with a resume JSON file to the specified URL.

    Args:
        resume_file_path (str): The path to the resume.json file.
        url (str): The URL to which the resume should be sent.
    """

    try:
        with open(resume_file_path, 'r') as resume_file:
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.put(url, data=resume_file, headers=headers)
            response.raise_for_status()
            print("Resume successfully uploaded!")
    except FileNotFoundError:
        print(f"Error: Resume file not found at '{resume_file_path}'")
    except requests.exceptions.RequestException as e:
        print(f"Error sending PUT request: {e}")


if __name__ == "__main__":
    resume_path = "./resume.json"
    target_url = "127.0.0.1:9002"

    send_resume_put(resume_path, target_url)