#!/usr/bin/env python3
from random import randint

def roll(number, dice_size):
    ans = 0
    try:
        for i in range(number):
            ans += randint(1,dice_size)
        return ans
    except:
        return 0

def gen_stat(option=None):
    """
    Generate one stat by rolling 4d6 and dropping the lowest
    """
    rolls = [roll(1,6) for x in range(4)]
    rolls.sort()
    return sum(rolls[1:])

def gen_stats():
    """
    Generate 6 stats for a new character
    """
    stat = [gen_stat() for x in range(6)]
    stat.sort(reverse=True)
    return stat

def roll_avg_stat(count):
    """
    return the average stat give a number of times run
    """
    avg = 0

    for i in range(count):
        avg += gen_stat()

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
