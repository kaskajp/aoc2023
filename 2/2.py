game_total_power = 0

with open('input.txt', 'r') as file:
    for line in file:
        sets = line.split(';')
        game_max_red = 0
        game_max_green = 0
        game_max_blue = 0
        game_power = 0
        for set in sets:
            if ':' in set:
                set = set[set.index(':')+1:]

            set_colors = set.split(',')
            for color_result in set_colors:
                split_color_result = color_result.split(' ')
                set_number = int(split_color_result[1].strip())
                set_color = split_color_result[2].strip()
                
                if set_color == 'red' and set_number > game_max_red:
                    game_max_red = set_number
                if set_color == 'green' and set_number > game_max_green:
                    game_max_green = set_number
                if set_color == 'blue' and set_number > game_max_blue:
                    game_max_blue = set_number
                    
        game_power = game_max_red * game_max_green * game_max_blue
        game_total_power += game_power

    print(game_total_power)