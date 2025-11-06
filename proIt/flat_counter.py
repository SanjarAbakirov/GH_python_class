flat_number = int(input("add number of the flat:"))


# entrance_number = (flat_number - 1) // 20 + 1
# floor_number = (flat_number - 1) % 20 // 4 + 1
# остаток от делдения кв деленная на кол во кв водном подьезде, 4 кв в подькзде

# Genka
entrance_number = (flat_number - 1) // 8 + 1
floor_number = (flat_number - 1) % 8 // 2 + 1


print("Подъезд №: %d" % (entrance_number))
print("Этаж №: %d" % (floor_number))
