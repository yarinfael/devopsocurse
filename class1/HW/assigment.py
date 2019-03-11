# A
first = 7
second = 44.3
print(first + second)
print(first * second)
print (second / first)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# B - my guess
a = 9
b = 8
c = 15
# B - check
a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print(a)
print(b)
print(c)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# C1 - There is no difference between the two since Python considers the " and ' as the same.
# C2 - can't print different data types. need to use str() (or delete the space and change the + to ,
my_number = 5+5
# use casting
print("result is: "+str(my_number))
# change the + to ,
print("result is:",my_number)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# D - 7, because casting 2.36 to int gives you 2
# check
# x = 5
# y = 2.36
# print(x + int(y))
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# E
x = input("please pick a number for x")
y = input("please pick a number for y")
if x > y:
    print("BIG")
if x < y:
    print("small")
if x == y:
    print("equal")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# F
num = int(input("pls pick a number between 1-4: "))
if num == 4:
    print("spring")
elif num == 3:
    print("fall")
elif num == 2:
    print("winter")
elif num == 1:
    print("summer")
else:
    print("error")
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Challenge
a=8
b="123"
# if you want the output to be a list -
print(a,b)
# if you want it to add one to the another -
print(a+int(b))
