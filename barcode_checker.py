# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Mandapat
# Section:      509
# Assignment:   11.11
# Date:         12 November 2023
#
def first(x):
    b = []
    for i in range(0, len(x) + 1, 2):
        b += [x[i]]
        # print(b)
    return b


def second(x):
    b = []
    for i in range(1, len(x), 2):
        b += [x[i]]
        # print(b)
    return b


fname = input("Enter the name of the file: ")
count = 0
valid = []
sum1 = 0
sum2 = 0
total = 0

with open(fname, "r") as f:
    lines = f.read().split('\n\n')
    for i in lines:
        i = i.replace("\n", " ")
        temp = i.split(" ")
        # print(temp)
        for j in range(len(temp)):
            j = str(temp[j])
            # print(j)
            first_half = first(j)
            second_half = second(j)
            last = int(first_half[-1])
            del first_half[-1]
            # print(first_half)
            # print(second_half)
            for k in first_half:
                sum1 += int(k)
            for l in second_half:
                sum2 += int(l)
            sum2 *= 3
            total = sum1 + sum2
            lastdigi = total % 10
            if 10 - lastdigi == last:
                count += 1
                valid.append(j)
            sum1 = 0
            sum2 = 0

    with open("valid_barcodes.txt", 'w') as w:
        for k in valid:
            w.write(k)
            w.write('\n')

print(f'There are {count} valid barcodes')
