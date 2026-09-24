from core.validators import is_valid_name
from core.base_module import BaseModule

class NameSearchModule(BaseModule):
    def run(self, target):
        if is_valid_name(target):
            return("[+]Starting name based search")
        else:
            return("[+]Invalid name parameter!")

    
if __name__ == "__main__":
    module = NameSearchModule()
    print(module.run("John Smith"))
    print(module.run("O'Brien"))
    print(module.run("12345"))
    print(module.run(""))