person = {"name": "Vamshi Krishna", "age": 21, "city": "Hyderabad"}

#Get values by key
print(person["name"])
print(person["age"])
print(person["city"])

#Safer with get()
print(person.get("job"))
print(person.get("hello", "Unknown"))