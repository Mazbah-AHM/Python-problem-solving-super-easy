data = input("Enter Your Number: ")

numberCount = 0
nonNumberCount = 0

for i in data:
    if i.isnumeric():
        numberCount += 1
    else:
        nonNumberCount += 1
print(f'Total Numeric data: {numberCount}')
print(f'Total Non-Numeric data: {nonNumberCount}')
