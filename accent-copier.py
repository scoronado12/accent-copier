#!/usr/bin/python
import pyperclip as cp
import sys

# Proof of Concept to assist in proper Spanish writing

spanish_chars = ["ñ", "á" , "é", "í", "ó", "ú" , "¿", "¡"]


def main():
    running = True
    
    while (running == True):
        print("Select a character to copy")
        print(" 1) ñ \t 2) á")
        print(" 2) é \t 3) í")
        print(" 4) ó \t 5) ú")
        print(" 6) ¿ \t 7) ¡")
            
        selection = input("Your Selection: ")
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
            cp.copy(spanish_chars[6])
            print("\n" * 100)
        elif(selection == "quit"):
            exit()
            

def charInCharOut(argv):
    
        if (argv == "n"):
            print(spanish_chars[0])
            return (spanish_chars[0])
            
        elif (argv == "a"):
            print(spanish_chars[1])
            return (spanish_chars[1])
            
        elif (argv == "i"):
            print(spanish_chars[2])
            return (spanish_chars[2])
            
        elif (argv == "o"):
            print(spanish_chars[3])
            return (spanish_chars[3])
            
        elif(argv == "u"):
            print(spanish_chars[4])
            return (spanish_chars[4])
            
        elif(argv == "?"):
            print(spanish_chars[5])
            return (spanish_chars[5])
        elif(argv == "!"):
            print(spanish_chars[6])
            return (spanish_chars[6])
            
    
    


            
if (__name__ == "__main__"):    
    if (len(sys.argv) > 1):
        cp.copy(charInCharOut(sys.argv[1]))
    else:
        main()
