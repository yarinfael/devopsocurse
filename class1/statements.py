a = 6
b = 8

# if a > b:
#     print(a,"is bigger than",b)
# if a < b:
#     print(b,"is bigger than",a)
# if a == b:
#     print(a,"is equal to",b)
#     if a >= 5:
#         print("5+")

if a > b:
    print("bigger")
elif a > 5:
    if a > 2:
        print("bigger than 2")
    elif a == 2:
        print("smaller than 2")
elif a < b:
    print("smaller")
elif a == b:
    print("equal")
else:
    print("none")



