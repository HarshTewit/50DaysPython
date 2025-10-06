def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid value please.")

numPeople = int(input("How many people are there in the group?"))
names = []
i = 1
while i <= numPeople:
    newName = input(f"Enter the name of the {i} person.")
    names.append(newName)
    i = i + 1

total = getFloat("Enter the total Amount.")

perPersonSplit = round(total/numPeople, 2)

for n in names:
    print(f"{n} owes {perPersonSplit}")

 