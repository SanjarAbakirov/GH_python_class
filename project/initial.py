# test
# def new_fn(name):
#     print(f"Hello, {name}")
# new_fn("Sam")



# def my_function():
#     print("Hellow from My fn")

# def some_fn_from_me():
#     print("Smbody called my fn")

# some_fn_from_me()
# my_function()

# arguments
# pattern
# def my_fn_args(username, greetings):
    # print("Hello, %s , from my Fn! with you %s"%(username, greetings))
# my_fn_args("Sam", "we do many things and projects")

# return values

# def sum_num(a, b):
#    return a + b

# def multy_num(a, b):
#    return a*b

# # 21*21 + 46*46

# print(sum_num(multy_num(21, 21), multy_num(46, 46)))


# Week 2 lection

# colors = ["red", "blue", "green", "white"]
# print(colors[0]) 
# print(colors[1])
# print(len(colors))

#  lists
# mylist = []

# mylist.append(1)
# mylist.append(2)
# mylist.append(3)
# # [1, 2, 3]
# mylist.append(4)

# print(mylist[0]) 
# print(mylist[1]) 
# print(mylist[2]) 
# print(mylist[3])

# insert
mylist2 = ['larry', 'curly', 'moe']
# mylist2.append('shrimp') 
# appended the element
# mylist2.insert(1, "Sammy")

# print(mylist2[0]) 
# print(mylist2[1]) 
# print(mylist2[2]) 
# print(mylist2[3])
# print(mylist2[4]) 

# extend
# mylist2.extend(["Horhe", "Karamba", "Misha"])
# mylist2.remove("larry")

# print(mylist2)
# print(mylist2.index("moe"))

mylist2.sort()
# print(mylist2)
mylist2.reverse()
# print(mylist2)
mylist2.pop(0)
# print(mylist2)

# my_element = mylist2.pop(1)
# print(my_element)

# inputs

# num = int(input())
# print(num)
# num_float = float(input())
# print(num_float)

string1 = input()
print(string1)

a = 5
b = 0.63
c = "hello"
print("a is : %d, b is %0.4f, c is %s" % (a,b,c))