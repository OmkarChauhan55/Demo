# # 1. Write a program to find the greatest of four numbers entered by the user.

# num1 = int(input("Enter the num"))

# num2 = int(input("Enter the num"))

# num3 = int(input("Enter the num"))

# num4 = int(input("Enter the num"))

# if(num1>num2 and num1>num3 and num1>num4):
#     print("The greatest number is:",num1)

# elif(num2>num1 and num2>num3 and num2>num4):
#     print("The greatest number is:",num2)

# elif(num3>num1 and num3>num2 and num3>num4):
#     print("The greatest number is:",num3)

# else:
#     print("The greatest number is:",num4)


# 2 Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# sub1 = int(input("Enter the marks"))

# sub2 = int(input("Enter the marks"))

# sub3 = int(input("Enter the marks"))


# marks= (sub1 + sub2 + sub3)/3
# print(marks)

# if(marks >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
#     print("Student is pass")

# else:
#     print("Student is fail")

# 3 A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams
# c1= "Make a lot of money" 
# c2= "buy now" 
# c3= "subscribe this" 
# c4= "click this"
# spam = input("Enter the comment:")


# if(c1 in spam or c2 in spam or c3 in spam or c4 in spam):
#     print("Spam comment")
# else:
#     print("Not spam")

# 4 Write a program to find whether a given username contains less than 10 characters or not.

# username = input("Enter username")

# if(len(username) < 10):
#     print("Username contain less than 10 char")
# else:
#     print("Username not contain less than 10 char")

# 5 Write a program which finds out whether a given name is present in a list or not

# l = ["Omkar", "Kuldip", "Rani"]

# n = input("Enter the name:")

# if( n in l):
#     print("Name is in list")
# else:
#     print("name is not in list")

# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# s1 = int(input("Enter the marks:"))
# s2 = int(input("Enter the marks:"))
# s3 = int(input("Enter the marks:"))
# s4 = int(input("Enter the marks:"))
# s5 = int(input("Enter the marks:"))

# total = (s1 + s2 + s3 + s4 + s5)/5
# print("The total percentage is:",total)

# if(total >=90 and total<=100):
#     print("Ex")
# elif(total >=80 and total<90):
#     print("A")
# elif(total >=70 and total<80):
#     print("B")
# elif(total >=60 and total<70):
#     print("C")
# elif(total >=50 and total<60):
#     print("D")
# else:
#     print("Fail")



# 7 Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Write the post:")

if("Harry".lower() in post.lower()):
    print("Harry is in post")
else:
    print("Harry is not post")
    