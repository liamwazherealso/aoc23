total = 0
for line in open("part_1.txt"):
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)

    total += int(digits[0] + digits[-1])

print(total)
