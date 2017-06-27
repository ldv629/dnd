#!/usr/bin/env python3
import dice

def print_help():
    print('List of Valid Commands:')
    print('\thelp')
    print('\texit')
    x = dir(dice)
    for y in x:
        if '__' in y or 'randint' in y:
            continue
        print('\t'+y,end='')
        if 'roll' is y:
            print('(num_of_dice,dice_size)')
        elif 'roll_avg' is y:
            print('(count,num_of_dice,dice_size)')
        elif 'roll_avg_stat' is y:
            print('(count)')
        elif 'gen' in y:
            print('()')
        else:
            print()

def main():

    print("Type 'help' to print commands")
    while(1):
        command = input('Enter a command to run: ',)
        if 'help' in command or 'randint' in command:
            print_help()
        elif 'exit' in command:
            return
        else:
            try:
                print(command + ': ' + str(eval('dice.'+command)))
            except:
                print_help()

if __name__ == "__main__":
   main() 
