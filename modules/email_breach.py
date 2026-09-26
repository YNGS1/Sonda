from core.validators import is_valid_email
from core.base_module import BaseModule
import hashlib
import requests

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

class EmailBreachModule(BaseModule):
    def run(self, target):
        if not is_valid_email(target):
            return {"Valid": False, "Message": "Invalid Email Address"}
        else:
            has_gravatar = check_gravatar(target)
            return {"Valid": True, "Gravatar": has_gravatar}

        
if __name__ == "__main__":
    module = EmailBreachModule()
    print(module.run("test@example.com"))
    print(module.run("твоя_реален_имейл_с_известен_gravatar"))
    print(module.run("12345"))