#!/usr/bin/python
import pyperclip as cp

# Proof of Concept to assist in proper Spanish writing

spanish_chars = ["ñ", "á" , "é", "í", "ó", "ú" , "¿", "¡"]

running = True

while (running == True):
    print("Select a character to copy")
    print(" 1) ñ \t 2) á")
    print(" 2) é \t 3) í")
    print(" 4) ó \t 5) ú")
    print(" 6) ¿ \t 7) ¡")
        
    selection = input("Your Selection ")
    if (selection == "1"):
        cp.copy(spanish_chars[0])
        print("\n" * 100)
    elif (selection == "2"):
        cp.copy(spanish_chars[1])
        print("\n" * 100)
    elif (selection == "3"):
        cp.copy(spanish_chars[2])
        print("\n" * 100)
    elif (selection == "4"):
        cp.copy(spanish_chars[3])
        print("\n" * 100)
    elif(selection == "5"):
        cp.copy(spanish_chars[4])
        print("\n" * 100)
    elif(selection == "6"):
        cp.copy(spanish_chars[5])
        print("\n" * 100)
    elif(selection == "7"):
        cp.copy(spanish_chars[5])
        print("\n" * 100)
    elif(selection == "quit"):
        exit()
