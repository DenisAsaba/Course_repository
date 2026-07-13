names = ["Alice", "Bob", "Charlie", "David", "Denis"]
print(names)
names[3] = "Daniel"  # Changing the fourth name from "David" to "Daniel"
print(names)

names.append("David")  # Adding a new name "David" to the end of the list
print(len(names))
print(names)

names.insert(2, "Eve")  # Inserting a new name "Eve" at index 2
print(len(names))
print(names)

names2 = ["Frank", "Grace", "Hannah", "Ivy", "Jack"]

names.extend(names2)  # Extending the names list with names2
print(len(names))
print(names)