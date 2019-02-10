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
    pass

def roll_purple(count):
    pass

def roll_red(count):
    pass

def roll_gold(count):
    pass

def roll_blue(count):
    pass

def roll_black(count):
    pass

def roll_white(count):
    pass

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


def starwars_print(result,color):
    print(color + ': ')
    print('\tadvantage: %d',result['advantage'])
    print('\tthreat: %d',result['threat'])
    print('\tsuccess: %d',result['success'])
    print('\tfailure: %d',result['failure'])
    
    print('\tforce: ')
    print('\t\tlight: %d',result['f

if __name__ == "__main__":
    import sys
    print("roll = {}".format(roll(int(sys.argv[1]),int(sys.argv[2]))))
