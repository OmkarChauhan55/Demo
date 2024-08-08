a = [1]
b = (1,) # (1) is int type but (1,) is tuple
 
print(type(a) ,"and ",type(b))


name = (22,4,5,6,4,"Omkar","hi")

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# name[1] = "hii"
# print(name) 
# problem
# #name[1] = "hii"
#     ~~~~^^^
# TypeError: 'tuple' object does not support item assignment

no = name.count(4)
print(no)

nos = name.index(22)
print(nos)