from modules.email_breach import EmailBreachModule
from modules.name_search import NameSearchModule   

available_modules = [EmailBreachModule(), NameSearchModule()]
target = input("Enter a search targert: ").strip()

results = {}    

for module in available_modules:
    print(repr(target))
    results[module.__class__.__name__] = module.run(target)
for name, result in results.items():
    print(f"{name}: {result}")