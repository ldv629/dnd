#!/usr/bin/env python3
import dice
import character_sheet
import dnd_db
import appJar

def main():
    """Main loop for gui"""

    dnd_db.create_db()

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
