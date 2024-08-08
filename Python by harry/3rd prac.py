# Write a python program to display a user enter name followed by good afternoon using input function 

name = input("Enter your name:")

print(f"Good Afternoon {name}") #f is f string used to add value of ther variable

# 2 Write a program to fill in a letter template given below with name and date

letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''
print(letter.replace("<|Name|>","omkar").replace("<|Date|>","23 jun"))

# Write a program to detect double space in a string.
name = "My name is  Omkar"

print(name.find("  "))

# Replace the double space from problem 3 with single spaces.
name = "My name is  Omkar"

print(name.replace("  "," "))

# Write a program to format the following letter using escape sequence characters.

letter = "Dear Harry,\n\tthis python course is nice.\nThanks!"
print(letter)