# Bill Calculator with people's names
people_list = []

name = str(input('Please insert your name'))
people =str(input('Please insert name of participants'))

bill = None
while bill is None:
    try:
        bill = float(input('enter the bill'))
    except ValueError:
        print("Error")

tipsPercent = bill/10
total = bill + tipsPercent

print("Hello, %s. Your Bill is %.2f and the tips is %.2f. Total amount bill is %.2f" % (name, bill, tipsPercent, total))


