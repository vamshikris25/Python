     #Repeat a specific number of times
#Print numbers from 0 to 4
#It counts from zero to Four
#Range - 5 means it prints 0-4 (known as indexes)
for i in range (5):
    print(i)




#Count from different starting points
#Count from 2 to 7
for i in range (2,8):
    print(i)

#Count by 2s:-
for i in range (0,10,2):
    print(i)

#Count by 5s:-
for i in range (0,45,5):
    print(i)

#Loop through text

name = "Vamshi"
for letter in name:
    print(letter)

#Loop through a list (preview - basics)
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(f"I like {color}")