from core.validators import is_valid_name
from core.base_module import BaseModule

class NameSearchModule(BaseModule):
    def run(self, target):
        if not is_valid_name(target):
            return{"Valid" : False , "Message" : "Invalid Name" }
        else:
            return{"Valid" : True , "Message" : "Valid Name"}

# if __name__ == "__main__":

#     module = NameSearchModule
#     print(module.run("Gencho Genchev"))


