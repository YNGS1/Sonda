import re
from core.base_module import BaseModule

class EmailBreachModule(BaseModule):
    def run(self, target):
        pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
        match = re.match(pattern, target)
        if match:
            return("[+]Beginning Search!")
        else:
            return("[+]Invalid Email Address")

if __name__ == "__main__":
    module = EmailBreachModule()
    print(module.run("test@email.com"))
    print(module.run("not_an_email"))