with open("input.txt") as f:
    scratchcard_scores = []
    for scratchcard in f:
        winning_nums, scratch_nums = scratchcard.split("|")
        winning_nums = [int(x) for x in winning_nums.split(":")[1].strip().split()]
        scratch_nums = [int(x) for x in scratch_nums.strip().split()]
        wins = sum([int(sn in winning_nums) for sn in scratch_nums])
        if wins:
            scratchcard_scores.append(pow(2, wins - 1))
        else:
            scratchcard_scores.append(0)

    print(sum(scratchcard_scores))

# sample.txt answer is 13
