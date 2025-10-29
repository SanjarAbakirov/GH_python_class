# name = str(input('Please inser your name'))
# bill = None
# while bill is None:
#     try:
#         bill = float(input('enter the bill'))
#     except ValueError:
#         print("Error")

# tipsPercent = bill/10
# total = bill + tipsPercent

# print("Hello, %s. Your Bill is %.2f and the tips is %.2f. Total amount bill is %.2f" % (name, bill, tipsPercent, total))

# -----------------
# Call the above functions with interesting inputs

# def main():
#     print('match_ends')
#     test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 1)
#     test(match_ends(['', 'x', 'xy', 'xyx', 'xx]), 2)
#     test(match_ends(['aaa', 'be', 'abc', 'hello']), 3)

    # print()
    # print('front_x')
    # test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    # test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    # test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    # print()
    # print('sort_last')
    # test(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    # test(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    # test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    
    # if __name__ == '__main__':
# main()


# a = str(input("insert Name"))
# b = int(input("insert integer"))
# c= float(input("insert a float number"))
# result = None

# def testFn(a, b, c):
#     f = b + c
#     return f
# result = testFn(a, b, c)
# print("Hello %s, your result is %.2f" % (a, result))

# -----------------

# def count(n):
#     if n == 0:
#         print('Engine!')
#     else:
#         print(n)
#         count(n-1)
# count(10)



