with open("input.txt") as almanac:
    lines = almanac.readlines()


da_rulez = []
for rules_text in lines[1:]:
    rules = [
        list(map(int, rule_line.split()))
        for rule_line in rules_text.split("\n")
        if ":" not in rule_line
    ]

    da_rulez.append(rules)


lines = "".join(lines).split("\n\n")
seed_pairs = list(map(int, lines[0].split(":")[1].strip().split()))
prev_min = None
for i in range(0, len(seed_pairs), 2):
    for input_resource in range(seed_pairs[i], seed_pairs[i] + seed_pairs[i + 1]):
        for rules_text in lines[1:]:
            for rule in rules:
                if input_resource >= rule[1] and input_resource < rule[1] + rule[2]:
                    input_resource = rule[0] + input_resource - rule[1]

        if prev_min is None:
            prev_min = input_resource
        else:
            prev_min = min(input_resource, prev_min)

print(prev_min)
