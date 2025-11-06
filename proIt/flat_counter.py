flat_number = int(input("add number of the flat:"))


entrance_number = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1
# остаток от делдения кв деленная на кол во кв водном подьезде

print(entrance_number)
print(floor_number)
