#!/usr/bin/env python3
import dice
import character_sheet
import dnd_db
import appJar

def main():
    """Main loop for gui"""

    dnd_db.create_db()

    dnd_app = appJar.gui()
    #Charcter dropdown
    #   Listing + add new

    #grid for stats
    dnd_app.go()
    while(1):
        break

if __name__ == "__main__":
   main() 
