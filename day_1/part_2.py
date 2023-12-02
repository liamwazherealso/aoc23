s2i = {
    3: {"one": "1", "two": "2", "six": "6"},
    4: {"four": "4", "five": "5", "nine": "9"},
    5: {"three": "3", "seven": "7", "eight": "8"},
}

total = 0


for line in open("input.txt"):
    digits = []
    line_len = len(line)
    for i in range(line_len):
        char = line[i]
        if char.isdigit():
            digits.append(char)
        else:
            for j in range(3, 6):
                j_len_digits = s2i[j]
                substring = line[i : i + j]
                if i + j < line_len and substring in j_len_digits:
                    digits.append(j_len_digits[substring])
                    break

    total += int(digits[0] + digits[-1])

print(total)
