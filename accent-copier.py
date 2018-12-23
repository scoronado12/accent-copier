#!/usr/bin/python
import pyperclip as cp
import sys


spanish_chars = dict(
                    zip(['a','e','i','o', 'n','u','?','!'],
                    ['á', 'é', 'í', 'ó', 'ñ', 'ú', '¿', '¡']))
        
def main():
    running = True
    
    while (running == True):
        print("Select a character to copy")
        print(" n) ñ \t a) á \n e) é \t i) í \n o) ó \t u) ú \n ?) ¿ \t !) ¡ \n q) quit")
        
        selection = input("Your Selection: ")

        try:
            if selection == 'q':
                exit()
            cp.copy(charInCharOut(selection))
            
        except KeyError:
            print("This is not a selection")
           

def charInCharOut(argv):
    
    '''pass in a char, return the corresponding char '''
    
    
    if argv in spanish_chars:
        char = spanish_chars[argv]
        print(char)
        return char
    
    print('Pass a proper char.')
    exit(1)

    


            
if (__name__ == "__main__"):    
    if (len(sys.argv) > 1):
        cp.copy(charInCharOut(sys.argv[1]))
    else:
        main()
