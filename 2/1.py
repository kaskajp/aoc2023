max_red = 12
max_green = 13
max_blue = 14

game_id_sum = 0

with open('input.txt', 'r') as file:
    for line in file:
        sets = line.split(';')
        game_id = sets[0].split(':')[0].split(' ')[1]
        for set in sets:
            if ':' in set:
                set = set[set.index(':')+1:]
                
            set_colors = set.split(',')
            color_results_ok = True
            for color_result in set_colors:
                split_color_result = color_result.split(' ')
                set_number = int(split_color_result[1].strip())
                set_color = split_color_result[2].strip()
                if set_color == 'red' and set_number > max_red:
                    color_results_ok = False
                    break
                if set_color == 'green' and set_number > max_green:
                    color_results_ok = False
                    break
                if set_color == 'blue' and set_number > max_blue:
                    color_results_ok = False
                    break
            
            if color_results_ok == False:
                break
            
        if color_results_ok:
            game_id_sum += int(game_id)
            continue
        
    print(game_id_sum)