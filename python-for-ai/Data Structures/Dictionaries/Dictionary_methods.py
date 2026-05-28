person = {"name": "Vamshi", "age": 21, "city": "Hyderabad"}

#Get all keys, values, or items
print(person.keys())     #dict_keys(['name', 'age', 'city'])
print(person.values())   #dict_values(['Vamshi', 21, 'Hyderabad'])
print(person.items())    #dict_items([('name', 'Vamshi'), ('age', 21), ('city', 'Hyderabad')])


#Check if a key exists
if "name" in person:
    print("name found!")


#Update multiple values
person.update({"age":31, "job": "Developer"})