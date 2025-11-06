# is_student = True
# is_graduated = False
# print(is_student)
# ----------------------
# x = 10
# y = 10
# print(x == y)
# is_equal = x != y
# print(is_equal)
# print(x < 5 and x > 2)
# ----------------------

# if True:
# print('Hello!')

# ----------------------

# x = 10
# if x > 0:
#     print("x is positive")
# elif x < 1:
#     print("x is negative")
# else:
#     print("x is zero")
# if conditions layer on top, the first condition will be executed

# ------------------------

# x = 10
# y = 10
# # if x > 0:
# #     if y > 0:
# #  it is better we need two conditions make iside sinle  conditions operator and put "and"
# if x > 0 and y > 0:
#     print("x & y are positive")

# -------------------------

# message = "Hello"
# if message:
# print("message is not empty")

# message1 = ""
# if bool(message1):
#     print("message is empty")

# -------------------------

# x = 0
# if x:
#     print("x is not zero")

# if we have empty str or zero value of a variabe - the code does not execute
# ------------------------


# --leap year -------

year = 2000

if year % 4 == 0 and year % 100 != 0:
    print("Leap year")
# здесь от пройдет без остатка но на 100 без остатака не разделится
elif year % 400 == 0:
    print("year is leap")
