#!/usr/bin/env python3
from random import randint

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

def gen_stat(option=None):
    """
    Generate one stat by rolling one of the following

    types of rolls:
        1d20
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
    else:
        rolls = [roll(1,6) for x in range(4)]
        rolls.sort()
        return sum(rolls[1:])

def gen_stats(option=None):
    """
    Generate 6 stats for a new character

    types of rolls:
        1d20
        3d6
        4d6 drop 1 (default)
        5d6 drop 2

    Input:
        optional input to select type of rolling
    Return:
        Integer
    """
    stat = [gen_stat(option) for x in range(6)]
    stat.sort(reverse=True)
    return stat

def roll_avg_stat(count,option=none):
    """
    return the average stat give a number of times run
    """
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

if __name__ == "__main__":
    import sys
    print("roll = {}".format(roll(int(sys.argv[1]),int(sys.argv[2]))))
