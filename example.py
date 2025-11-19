# my_operation = "read"
# if my_operation == "read":
#     print("perform read operation…")
# elif my_operation == "update":
#     print("perform update operation …")
# elif my_operation == "insert":
#     print("perform insert operation …")
# elif my_operation == "delete":
#     print ("perform delete operation …")
# else:
#     print("wrong variant if operation !!! ")
#
#
# my_operation = "read"
# match my_operation:
#     case "read":
#         print("perform read operation…")
#     case "update":
#         print("perform update operation …")
#     case "insert":
#         print("perform insert operation …")
#     case "delete":
#         print("perform delete operation …")
#     case _:
#         print("wrong variant if operation !!!")
#
# nothing = None
# print(type(nothing))
#
# x = int(input("Please input 0 to stop iteration: "))
# sum_result = 0
# while x:
#     sum_result += x
#     x = int(input("Please input 0 to stop iteration: "))
# print(sum_result)


n = int(input("Input integer number: "))
sum_result = 0
x = 1

while x < n:
    x += 1
    if x % 2:
        continue
    sum_result += x

print(f"Sum of even numbers: {sum_result}")