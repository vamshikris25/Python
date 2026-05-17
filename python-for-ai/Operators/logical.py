#AND
age = 18

has_license = False

can_drive = age >=16 and has_license
print(can_drive) #False

#OR
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend) #True

#NOT
is_adult = age >=18
is_child = not is_adult
print(is_child) #False