from core.validators import is_valid_name
from core.base_module import BaseModule

class NameSearchModule(BaseModule):
    def run(self, target):
        if is_valid_name(target):
            return("[+]Starting name based search")
        else:
            return("[+]Invalid name parameter!")
