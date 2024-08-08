# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

# words = { 
#     "Apple": "Seph",
#     "Mango": "Aam",
#     "Banana": "Kela",
# }

# word = input("Enter the word you want meaning:")
# print(words[word])

# 2 Write a program to input eight numbers from the user and display all the unique numbers (once).

# se = set()

# s = (input("Enter the number"))
# se.add(int(s))
# s = (input("Enter the number"))
# se.add(int(s))
# s = (input("Enter the number"))
# se.add(int(s))
# s = (input("Enter the number"))
# se.add(int(s))
# s = (input("Enter the number"))
# se.add(int(s))
# s = (input("Enter the number"))
# se.add(int(s))

# print(se)

# Can we have a set with 18 (int) and '18' (str) as a value in it?

# se = set()

# se.add(18)
# se.add("18")
# print(se)

# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# print(s)

# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter friend name:")
lang = input("Enter language name:")

d.update({name: lang})

name = input("Enter friend name:")
lang = input("Enter language name:")

d.update({name: lang})

name = input("Enter friend name:")
lang = input("Enter language name:")

d.update({name: lang})

name = input("Enter friend name:")
lang = input("Enter language name:")

d.update({name: lang})

print(d)

# 7 If the names of 2 friends are same; what will happen to the program in problem 6?

# then the second name is print only {'om': 'c', 'kul': 'c++', 'ayu': 'java'}


# 8 If languages of two friends are same; what will happen to the program in problem 6?
# {'om': 'python', 'kul': 'python', 'kk': 'gg', 'bb': 'vv'} All is print

# 9 Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

# not possible cannot change