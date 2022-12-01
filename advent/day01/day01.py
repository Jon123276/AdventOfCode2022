addhere = 0
currentTotal1 = 0
currentTotal2 = 0
currentTotal3 = 0
with open("input.txt") as file:
    for line in file:
        if line == "\n":
            if currentTotal1 < addhere:
                currentTotal1 = addhere
            elif currentTotal1 > addhere and currentTotal2 < addhere:
                currentTotal2 = addhere
            elif currentTotal2 > addhere and currentTotal3 < addhere:
                currentTotal3 = addhere
            addhere = 0
            print("Current Totals: " + str(currentTotal1) + ", " + str(currentTotal2) + ", " + str(currentTotal3), end="\n")
            continue
        addhere = addhere + int(line)


print(currentTotal1 + currentTotal2 + currentTotal3)
