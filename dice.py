#!/usr/bin/env python3

from random import randint

import character_sheet
import math

def roll(number, dice_size):
    """
    Rolls the dice

    Input:
        number -- number of dice to roll
        dice_size -- sides on the dice desired to be rolled
    Return:
        0 if invalid
        sum of the resulting dice roll

    Possible TODO: return list of rolls and sum
    """

    ans = 0
    try:
        for i in range(number):
            ans += randint(1,dice_size)
        return ans
    except:
        return 0

def roll_advantage(stat_user=None):
    """ 
    Rolls a d20 with advantage rules from 5th edition

    Input:
        stat_user -- tuple for stat and user id (Optional)
    Return:
        Hgher of two rolls
    """
    if stat_user == None:
        r1 = roll(1,20)
        r2 = roll(1,20)
    else:
        r1 = roll_stat(stat_user[0], stat_user[1])
        r2 = roll_stat(stat_user[0], stat_user[1])

    return r1 if r1 > r2 else r2 

def roll_disadvantage(stat_user=None):
    """ 
    Rolls a d20 with disadvantage rules from 5th edition

    Input:
        stat_user -- tuple for stat and user id (Optional)
    Return:
        Lower of two rolls
    """
    if stat_user == None:
        r1 = roll(1,20)
        r2 = roll(1,20)
    else:
        r1 = roll_stat(stat_user[0], stat_user[1])
        r2 = roll_stat(stat_user[0], stat_user[1])

    return r1 if r1 < r2 else r2 

def roll_stat(stat, user_id):
    """
    Roll stat/ability for character
    Return:
        roll + stat
    """
    return roll(1,20) + character_sheet.get_stat(stat, user_id)

def roll_skill(skill, user_id):
    """
    Roll skill for character
    Return:
        roll + skill
    """
    return roll(1,20) + character_sheet.get_skill(stat, user_id)

def roll_save(save,user_id):
    """
    Roll save for character
    Return:
        roll + save
    """
    return roll(1,20) + character_sheet.get_save(save, user_id)

def roll_init(user_id):
    """
    Roll init for character
    Return:
        roll + init
    """
    return dice.roll(1,20) + character_sheet.get_init(user_id)

def gen_stat(option=None):
    """
    Generate one stat by rolling one of the following

    types of rolls:
        1d20
        2d6+6
        3d6
        4d6 drop 1 (default)
        5d6 drop 2

    Input:
        optional input to select type of rolling
    Return:
        Integer
    """

    if '3d6' == option:
        rolls = [roll(1,6) for x in range(3)]
        return sum(rolls)
    elif '5d6' == option:
        rolls = [roll(1,6) for x in range(5)]
        rolls.sort()
        return sum(rolls[2:])
    elif '1d20' == option:
        return roll(1,20)
    elif '2d6+6' == option:
        return roll(1,6) + roll(1,6) + 6
    else: #4d6 drop one
        rolls = [roll(1,6) for x in range(4)]
        rolls.sort()
        return sum(rolls[1:])

def gen_stats(option=None):
    """
    Generate 6 stats for a new character

    types of rolls:
        1d20
        2d6+6
        3d6
        4d6 drop 1 (default)
        4d6 drop 1 seven times drop lowest
        5d6 drop 2

    Input:
        optional input to select type of rolling
    Return:
        Integer
    """
    if option == '4d6x7':
        stat = [gen_stat('4d6') for x in range(7)]
        stat.sort(reverse=True)
        stat = stat[:-1]
    else:
        stat = [gen_stat(option) for x in range(6)]
        stat.sort(reverse=True)

    return stat

def calc_modifiers(stats):
    """ returns a list of all the stat modifiers for a list of ability scores """
    return [stat_mod(x) for x in stats]

def stat_mod(stat):
    """ return the calculated stat modifier """
    return math.floor((stat-10)/2)

def roll_avg_stat(count,option=None):
    """ return the average stat give a number of times run """
    avg = 0

    for i in range(count):
        avg += gen_stat(option)

    return avg / count


def roll_avg(count, number, dice_size):
    """
    return the average roll for a dice size and number of dice
    """
    avg = 0

    for i in range(count):
        avg += roll(number, dice_size)

    return avg / count

########Star Wars Dice##################
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

if __name__ == "__main__":
    import sys
    print("roll = {}".format(roll(int(sys.argv[1]),int(sys.argv[2]))))
