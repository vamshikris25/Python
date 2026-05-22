#Empty list

my_list = []

#List with items
fruits = ["apple", "banana", "orange"]
numbers = [1,2,3,4,5]
mixed = ["hello", 42, True, 3.14]


age = "Age"
has_license = True

my_list = ["Alice", 21, age , True, has_license]

my_list[0] = "Vamshi"


my_list.insert(1, "Krishna")


#Changing lists

fruits = ["apple", "banana", "orange"]

#Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

#Add items
fruits.append("grape")  #Add to end
fruits.insert(1, "kiwi")  #Insert at position

#Remove items
fruits.remove("banana")  #Remvoves banana
last = fruits.pop()      #Remove and return last
del fruits[0]            #Remove by index
print(fruits)

#List methods

numbers = [3,1,4,1,5,9]

#Information
print(len(numbers))        #6 - Length
print(numbers.count(1))    #2 - Occurances
print(numbers.index(4))    #2 - Find position

#Sorting
numbers.sort()       # Sorts in place
print(numbers)       # [1,1,3,4,5,9]

numbers.reverse()    # Reverse Order
print(numbers)       # [9,5,4,3,1,1]

#Copy
new_list = numbers.copy()  #Creates a copy


#Checking lists
fruits = ["apple", "banana", "orange"]

#Check if item exists
if "apple" in fruits:
    print("Apple found!")
else:
    print("Not found!")

#Check if list is empty
if fruits:
    print("List has items")

else:
    print("List is empty")


    