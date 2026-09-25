import hashlib
import requests

email = input("Please enter a valid email address: ")

def check_gravatar(email):
    normalized_email = email.strip().lower()
    email_bytes = normalized_email.encode('utf-8')
    hash_result = hashlib.md5(email_bytes).hexdigest()
    url = "https://www.gravatar.com/avatar/" + hash_result + "?d=404"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False

if __name__ == "__main__":
    email = input("Please enter a valid email address: ")
    print(check_gravatar(email))