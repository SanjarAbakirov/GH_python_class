# # Bill Calculator with people's names
list = []

name = str(input('Please insert your name'))
people = str(input('Please insert name of participants'))
list.append(people)
num = len(list[0].split())

bill = None
while bill is None:
    try:
        bill = float(input('enter the bill'))
    except ValueError:
        print("Error")

tips = bill/10

def thanks(tips):
    if tips > 20:
        return "Thank you for your generosity!"


total = (bill + tips)
share = total/num

print("Hello, %s. Your Bill is %.2f and the tips is %.2f. Total amount bill is %.2f. The share from each is: %d. %s" % (name, bill, tips, total, share, thanks(tips)))



# Lesson #4 logical operators

# boolean
# x = 2
# print(x == 2) # prints true by default
# print(x == 3) # prints false by default
# print(x < 3) # prints true by default


