#!/usr/bin/env python3

from dice import roll

def roll_green(count):
    result = {'advantage':0, 'success':0}
    for x in range(count):
        num = roll(1, 8)
        if num == 1:
            pass
        elif num == 2:
            result['advantage'] += 1
        elif num == 3:
            result['advantage'] += 1
        elif num == 4:
            result['advantage'] += 2
        elif num == 5:
            result['advantage'] += 1
            result['success'] += 1
        elif num == 6:
            result['success'] += 1
        elif num == 7:
            result['success'] += 1
        elif num == 8:
            result['success'] += 2
    return result

def roll_purple(count):
    result = {'threat':0, 'failure':0}
    for x in range(count):
        num = roll(1, 8)
        if num == 1:
            pass
        elif num == 2:
            result['threat'] += 1
        elif num == 3:
            result['threat'] += 1
        elif num == 4:
            result['threat'] += 2
        elif num == 5:
            result['threat'] += 1
            result['failure'] += 1
        elif num == 6:
            result['failure'] += 1
        elif num == 7:
            result['failure'] += 1
        elif num == 8:
            result['failure'] += 2
    return result

def roll_red(count):
    result = {'threat':0, 'failure':0, 'despair':0}
    for x in range(count):
        num = roll(1, 12)
        if num == 1:
            pass
        elif num == 2:
            result['threat'] += 1
        elif num == 3:
            result['threat'] += 1
        elif num == 4:
            result['threat'] += 2
        elif num == 5:
            result['threat'] += 2
        elif num == 6:
            result['threat'] += 1
            result['failure'] += 1
        elif num == 7:
            result['threat'] += 1
            result['failure'] += 1
        elif num == 8:
            result['failure'] += 1
        elif num == 9:
            result['failure'] += 1
        elif num == 10:
            result['failure'] += 2
        elif num == 11:
            result['failure'] += 2
        elif num == 12:
            result['despair'] += 1
    return result

def roll_gold(count):
    result = {'advantage':0, 'success':0, 'triumph':0}
    for x in range(count):
        num = roll(1, 12)
        if num == 1:
            pass
        elif num == 2:
            result['advantage'] += 1
        elif num == 3:
            result['advantage'] += 1
        elif num == 4:
            result['advantage'] += 2
        elif num == 5:
            result['advantage'] += 2
        elif num == 6:
            result['advantage'] += 1
            result['success'] += 1
        elif num == 7:
            result['advantage'] += 1
            result['success'] += 1
        elif num == 8:
            result['success'] += 1
        elif num == 9:
            result['success'] += 1
        elif num == 10:
            result['success'] += 2
        elif num == 11:
            result['success'] += 2
        elif num == 12:
            result['triumph'] += 1
    return result

def roll_blue(count):
    result = {'advantage':0, 'success':0}
    for x in range(count):
        num = roll(1, 6)
        if num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            result['advantage'] += 1
        elif num == 4:
            result['advantage'] += 2
        elif num == 5:
            result['advantage'] += 1
            result['success'] += 1
        elif num == 6:
            result['success'] += 1
    return result

def roll_black(count):
    result = {'threat':0, 'failure':0}
    for x in range(count):
        num = roll(1, 6)
        if num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            result['threat'] += 1
        elif num == 4:
            result['threat'] += 2
        elif num == 5:
            result['threat'] += 1
            result['failure'] += 1
        elif num == 6:
            result['failure'] += 1
    return result

def roll_white(count):
    result = {'dark':0, 'light':0}
    for x in range(count):
        num = roll(1, 12)
        if num == 1:
            result['dark'] += 1
        elif num == 2:
            result['dark'] += 1
        elif num == 3:
            result['dark'] += 1
        elif num == 4:
            result['dark'] += 1
        elif num == 5:
            result['dark'] += 1
        elif num == 6:
            result['dark'] += 1
        elif num == 7:
            result['dark'] += 2
        elif num == 8:
            result['light'] += 1
        elif num == 9:
            result['light'] += 1
        elif num == 10:
            result['light'] += 2
        elif num == 11:
            result['light'] += 2
        elif num == 12:
            result['light'] += 2
    return result

def roll_starwars(green,purple,blue,black,gold,red,white):
    green_result = roll_green(green)
    purple_result = roll_purple(purple)
    blue_result = roll_blue(blue)
    black_result = roll_black(black)
    gold_result = roll_gold(gold)
    red_result = roll_red(red)
    white_result = roll_white(white)

    result = {  'green' :   green_result,
                'purple':   purple_result,
                'blue'  :   blue_result,
                'black' :   black_result,
                'gold'  :   gold_result,
                'red'   :   red_result,
                'white' :   white_result}

    return result

def starwars_print_net(result):
    at_result = result['green']['advantage'] + \
                result['blue']['advantage'] + \
                result['gold']['advantage'] - \
                result['purple']['threat'] - \
                result['black']['threat'] - \
                result['red']['threat']

    sf_result = result['green']['success'] + \
                result['blue']['success'] + \
                result['gold']['success'] - \
                result['purple']['failure'] - \
                result['black']['failure'] - \
                result['red']['failure']

    td_result = result['gold']['triumph'] - result['red']['despair']

    print('Net Advantage/Threat: %d', at_result)
    print('Net Success/Failure: %d', sf_result)
    print('Net Triumph/Despair: %d', td_result)
    print('Lightside: %d', result['white']['light'])
    print('Darkside: %d', result['white']['dark'])
    

   

def starwars_print(result,color):
    #TODO:fix
    print(color + ': ')
    if color != 'white':
        print('\tadvantage: %d',result[color]['advantage'])
        print('\tthreat: %d',result[color]['threat'])
        print('\tsuccess: %d',result[color]['success'])
        print('\tfailure: %d',result[color]['failure'])
        print('\ttriumph: %d',result[color]['triumph'])
        print('\tdespair: %d',result[color]['despair'])
    else:
        print('\tforce: ')
        print('\t\tlight: %d',result[color]['light'])
        print('\t\tdark: %d',result[color]['dark'])
