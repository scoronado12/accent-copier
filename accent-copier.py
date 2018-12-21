#!/usr/bin/python
import pyperclip as cp
import sys

# Proof of Concept to assist in proper Spanish writing

spanish_chars = ["ñ", "á" , "é", "í", "ó", "ú" , "¿", "¡"]


def main():
    running = True
    
    while (running == True):
        print("Select a character to copy")
        print(" 1) ñ \t 2) á \n 3) é \t 4) í \n 5) ó \t 6) ú \n 7) ¿ \t 8) ¡")
            
        selection = input("Your Selection: ")
        if (selection == "1"):
            cp.copy(spanish_chars[0])
            print("Selected " + spanish_chars[0])
        elif (selection == "2"):
            cp.copy(spanish_chars[1])
            print("Selected " + spanish_chars[1])
        elif (selection == "3"):
            cp.copy(spanish_chars[2])
            print("Selected " + spanish_chars[2])
        elif (selection == "4"):
            cp.copy(spanish_chars[3])
            print("Selected " + spanish_chars[3])
        elif(selection == "5"):
            cp.copy(spanish_chars[4])
            print("Selected " + spanish_chars[4])
        elif(selection == "6"):
            cp.copy(spanish_chars[5])
            print("Selected " + spanish_chars[5])
        elif(selection == "7"):
            cp.copy(spanish_chars[6])
            print("Selected " + spanish_chars[6])
            print("Selected " + spanish_chars[6])
        elif(selection == "8"):
            print("Selected " + spanish_chars[7])
            print("Selected " + spanish_chars[7])
        elif((selection == "quit") or (selection == "q")):
            print("¡Chau!")
            exit()
        else:
            print("Nothing Selected")
                        

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
