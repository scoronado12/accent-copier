#!/usr/bin/python
import pyperclip as cp
import sys


#spanish_chars = ["ñ", "á" , "é", "í", "ó", "ú" , "¿", "¡"]
spanish_chars = dict(
                    zip(['a','e','i','o', 'n','u','?','!'],
                    ['á', 'é', 'í', 'ó', 'ñ', 'ú', '¿', '¡']))
        
def main():
    running = True
    
    while (running == True):
        print("Select a character to copy")
        print(" n) ñ \t a) á \n e) é \t i) í \n o) ó \t u) ú \n ?) ¿ \t !) ¡ \n q) quit")
        
        
        
        
        
        
        selection = input("Your Selection: ")

        
        print(selection)
        charInCharOut(spanish_chars[selection])
        
        
        '''
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
        elif(selection == "8"):
            print("Selected " + spanish_chars[7])
            cp.copy(spanish_chars[7])
        elif((selection == "quit") or (selection == "q")):
            print("¡Chau!")
            exit(0)
        else:
            print("Nothing Selected")
           '''             

def charInCharOut(argv):
    
    if argv not in spanish_chars:
        print('Pass a proper char.')
        exit(1)
    
    char = spanish_chars[argv]
    print(char)
    return char

    


            
if (__name__ == "__main__"):    
    if (len(sys.argv) > 1):
        cp.copy(charInCharOut(sys.argv[1]))
    else:
        main()
