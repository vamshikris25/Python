person = {"name": "alice", "age": 30}

#Add or Update

person["email"] = "vamshikris25@gmail.com"    #Add New
person["age"] = 21                            #Update existing
person["name"] = "Vamshi Krishna"

#Remove items
del person ["email"]                          #Remove by key
age = person.pop("age")                       #Remove and return 
person.clear()                                #Removes all items
