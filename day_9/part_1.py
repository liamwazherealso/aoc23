# sample.txt answer is 114

with open("input.txt") as f:
    histories = f.readlines()


predicted_values = 0
for history in histories:
    delta_step = []

    curr_step = list(map(int, history.strip().split()))

    # Calculate step history
    while sum(curr_step):
        delta_step.append(curr_step)
        curr_step = [curr_step[i + 1] - curr_step[i] for i in range(len(curr_step) - 1)]

    # Calculate predicted value
    if len(delta_step) == 1:
        predicted_values.append(0)
        continue

    for step in delta_step:
        print(" ".join(map(str, step)))

    delta_step = delta_step[::-1]

    predicted_value = 0
    for step in delta_step:
        print(predicted_values)
        predicted_values += step[-1]

print(predicted_values)
