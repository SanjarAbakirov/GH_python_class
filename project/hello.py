# HW_W_1

# Homework W1
# Task_1

# print("Hellow world")
# print("Hellow Alice")

# Task_2

# x = 1
# if x == 1:
    # intended four spaces
    # print("x is 1")

# Task_2 Alice

def greetings_Alice():
    print("Somebody is calling Alice")
# greetings_Alice()

# Task 3 change "Hello" for "Howdy"

"""A tiny Python program to check that Python is working. Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

# def greet_fn(name, extra_word):
    # print("Hello, " + name + ". Welcome and " + extra_word)

# greet_fn("Sam", "Have a good day")

# first way
# def function_alice(greeting, name):
    # print("%s, %s"%(greeting, name))
# function_alice("Hello", "Alice")
# function_alice("Howdy", "Alice")

# second way
# def fn_greet_alice(greeting, name):
    # print(greeting + ". " + name)
# fn_greet_alice("Hello", "Alice")
# fn_greet_alice("Howdy", "Alice")


# second task
# # Define a main() function that prints a little greeting.
# def main():
#   # Get the name from the command line, using 'World' as a fallback.
#   if len(sys.argv) >= 2:
#     name = sys.argv[1]
#   else:
#     name = 'World'
#   print('Hello', name)

# # This is the standard boilerplate that calls the main() function.
# if __name__ == '__main__':
#   main()


# Donuts function
# import sys

def main():
  num_don = int(input('How many donuts?'))
  if num_don <= 9:
    # num_don = sys.argv[1]
    print("Number of donuts:", + num_don),
  else:
    print("You eat too many of them")

if __name__ == '__main__':
# Код, который выполняется только при прямом запуске (например, main()),
# и код (функции, классы), который можно использовать при импорте, не вызывая побочных эффектов.
# «Если этот файл запущен напрямую (а не импортирован), то вызови функцию main()».
  main()
