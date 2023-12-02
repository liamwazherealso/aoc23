game_powers = []
from collections import 
with open("input.txt") as f:
    for line in f:
        game_id = int(line.split(":")[0].split(" ")[1])

        draws = line.split(":")[1].split(";")

        min_cube = 
        for draw in draws:
            for color_draw in draw.split(","):
                color_draw = color_draw.strip()
                num, color = color_draw.split(" ")
                num = int(num)
                if color not in min_cube:
                    min_cube[color] = num
                else:
                    min_cube[color] = max(min_cube[color], num)

        game_power = 1
        for min_cube_num in min_cube.values():
            game_power *= min_cube_num
        game_powers.append(game_power)

print(sum(game_powers))
