from core.validators import is_valid_email
from core.base_module import BaseModule

class EmailBreachModule(BaseModule):
    def run(self, target):
        if is_valid_email(target):
            return("[+]Beginning Search!")
        else:
            return("[+]Invalid Email Address")
