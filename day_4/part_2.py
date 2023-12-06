from collections import defaultdict

with open("input.txt") as f:
    scratchcard_scores = []
    card_queue = list()
    scratchcard_count = defaultdict(int)
    collected_cards = 0

    for scratchcard in f:
        card_and_winning_nums, scratch_nums = scratchcard.split("|")
        card_no, winning_nums = card_and_winning_nums.split(":")
        card_no = int(card_no.split()[1])

        winning_nums = winning_nums.split()
        scratch_nums = scratch_nums.split()

        wins = sum([int(sn in winning_nums) for sn in scratch_nums])

        scratchcard_count[card_no] += 1
        for increment in range(1, wins + 1):
            scratchcard_count[card_no + increment] += scratchcard_count[card_no]

print(sum(scratchcard_count.values()))
