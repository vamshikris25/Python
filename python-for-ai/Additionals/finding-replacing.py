message = "I love Python programming in VS Code (Code Editor)"

#To check something
print("Python" in message)
print(message.startswith("I"))
print(message.endswith("Python"))

#Finding the position
print(message.find("python"))
print(message.count("Code"))

#Replacing
new_message = message.replace("Python","SQL")
print(new_message)