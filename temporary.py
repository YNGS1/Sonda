text = "EmailBreachModule, NameSearchModule"
parts = text.split(",")

selected_names = []
for part in parts:
    selected_names.append(part.strip())

print(selected_names)