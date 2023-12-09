# sample.txt answer is 2

with open("input.txt") as f:
    histories = f.readlines()


predicted_values = []
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

    delta_step = delta_step[::-1]

    predicted_value = 0
    for step in delta_step:
        predicted_value = step[0] - predicted_value
        print(predicted_value)

    predicted_values.append(predicted_value)

print(sum(predicted_values))
