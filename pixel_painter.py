# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Mandapat
# Section:      509
# Assignment:   11.12
# Date:         12 November 2023
#

fname = input("Enter the filename: ")
# fname = "pixel_triangle.csv"
char = input("Enter a character: ")
# char = "A"
total = ""
name = fname.split(".csv") # use name[0] for written file name
with open(fname, "r") as f:
    lines = f.read().split("\n")
    # print(lines)
    for i in lines:
        ln = ""
        i = i.split(",")
        # print(i)
        for j in range(len(i)):
            # print(j)
            if j % 2 == 0:
                ln += " " * int(i[j])
                # print(ln)
            else:
                ln += char * int(i[j])
                # print(ln)
        ln += "\n"
        total += ln
    # print(total)
    with open(name[0] + ".txt", "w") as w:
        for k in total:
            w.write(k)

print(f'{name[0] + ".txt"} created!')

