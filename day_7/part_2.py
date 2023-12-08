from collections import Counter, defaultdict

with open("input.txt") as f:
    bids_and_bid_count = [line.split() for line in f.readlines()]

# Organize bids_and_bid_count into a list of [Counter(bid), bid_count]
bid_count_amount = [
    [bid, Counter(bid), bid_count] for bid, bid_count in bids_and_bid_count
]

# Organize bids_and_bid_count into a dictionary of {hand: [bid_count, ...]}
hand_dict = defaultdict(list)

for bid, bind_count, bid_count in bid_count_amount:
    j_count = bind_count["J"]
    if "J" in bind_count:
        del bind_count["J"]

    if not bind_count:
        hand_dict[5].append([bid, bid_count])
        continue
    hand_key = tuple(sorted(bind_count.values()))

    last, second_last = hand_key[-1] + j_count, hand_key[-2] if len(hand_key) > 1 else 0
    if (last == 3 and second_last != 2) or (last == 2 and second_last == 2):
        # three of a kind becomes 2
        # two of a kind become 1
        hand_key = last - 1
        print("1")
    elif last <= 2:
        # pair becomes 0, high card becomes 1
        hand_key = last - 2
        print("2")
    else:
        hand_key = last

        print("3")
    print(hand_key == last)
    print(bid, j_count, second_last, last, hand_key)
    hand_dict[hand_key].append([bid, bid_count])
    print("=======")
print("====")

card_strength = "J23456789TQKA"

bids_amounts_ordered = []


def strength_sort(s: str):
    # reverse string
    s = s[-1::-1]

    return sum([pow(13, i) * card_strength.index(card) for i, card in enumerate(s)])


hands_ordered = []
for hand_key, bid_count_amount in dict(sorted(hand_dict.items())).items():
    sorted_list = sorted(bid_count_amount, key=lambda x: strength_sort(x[0]))

    print(sorted_list)
    hands_ordered.extend([bid_amount for _, bid_amount in sorted_list])

print(hands_ordered)

total = 0
for i, bid_amount in enumerate(hands_ordered):
    total += (i + 1) * int(bid_amount)
print(total)
