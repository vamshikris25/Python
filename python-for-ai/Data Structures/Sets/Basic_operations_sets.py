colors = {"red", "blue"}

#Add items
colors.add("green")
print(colors)

#Remove items
colors.remove("white")     #Error if not found
colors.discard("yellow")   #No error if not found

#Check membership
if "red" in colors:
    print("Red is available")