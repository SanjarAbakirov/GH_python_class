flat_number = int(input("add number of the flat:"))


# entrance_number = (flat_number - 1) // 20 + 1
# floor_number = (flat_number - 1) % 20 // 4 + 1
# остаток от делдения кв деленная на кол во кв водном подьезде, 4 кв в подькзде

entrance_number = (flat_number - 1) // 8 + 1
floor_number = (flat_number - 1) % 8 // 2 + 1


print(entrance_number)
print(floor_number)
