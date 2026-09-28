from modules.email_breach import EmailBreachModule
from modules.name_search import NameSearchModule   

available_modules = [EmailBreachModule(), NameSearchModule()]
target = input("Enter a search target: ").strip()

text = input("Enter a module to run (comma separated): ")

parts = text.split(",")

selected_names = []
for part in parts:
    selected_names.append(part.strip())
print(selected_names)

filtered_modules = []
 

for module in available_modules:
    if module.__class__.__name__ in selected_names:
        filtered_modules.append(module)

print([m.__class__.__name__ for m in filtered_modules])
results = {}   

for module in filtered_modules:
    results[module.__class__.__name__] = module.run(target)

for name, result in results.items():
    print(f"{name}: {result}")
