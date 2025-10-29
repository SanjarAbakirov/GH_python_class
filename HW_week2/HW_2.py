bill = None
while bill is None:
    try:
	    bill = float(input('enter the bill'))
    except ValueError:
        print("Error")

tipsPercent = bill/10
total = bill + tipsPercent

print("Bill: %.2f. Tips: %.2f. Total: %.2f" % (bill, tipsPercent, total))