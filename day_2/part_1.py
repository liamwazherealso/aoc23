max_cube = {"red": 12, "blue": 14, "green": 13}
valid_games = []
with open("input.txt") as f:
    for line in f:
        game_id = int(line.split(":")[0].split(" ")[1])

        valid = True
        draws = line.split(":")[1].split(";")
        for draw in draws:
            print(draw)
            for color_draw in draw.split(","):
                color_draw = color_draw.strip()
                num, color = color_draw.split(" ")
                num = int(num)
                if num > max_cube[color]:
                    valid = False
        if valid:
            valid_games.append(game_id)

print(sum(valid_games))
