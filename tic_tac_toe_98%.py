import random, os
from os import system as shell
#if __name__ == "__main__":
def printBoard(Xvar, Ovar):
        ZERO = '\033[1;31mX\033[0m' if Xvar[0] else("\033[1;34mO\033[0m" if Ovar[0] else 0)
        st1 = '\033[1;31mX\033[0m' if Xvar[1] else("\033[1;34mO\033[0m" if Ovar[1] else 1)
        nd2 = '\033[1;31mX\033[0m' if Xvar[2] else("\033[1;34mO\033[0m" if Ovar[2] else 2)
        rd3 = '\033[1;31mX\033[0m' if Xvar[3] else("\033[1;34mO\033[0m" if Ovar[3] else 3)
        th4 = '\033[1;31mX\033[0m' if Xvar[4] else("\033[1;34mO\033[0m" if Ovar[4] else 4)
        th5 = '\033[1;31mX\033[0m' if Xvar[5] else("\033[1;34mO\033[0m" if Ovar[5] else 5)
        th6 = '\033[1;31mX\033[0m' if Xvar[6] else("\033[1;34mO\033[0m" if Ovar[6] else 6)
        th7 = '\033[1;31mX\033[0m' if Xvar[7] else("\033[1;34mO\033[0m" if Ovar[7] else 7)
        th8 = '\033[1;31mX\033[0m' if Xvar[8] else("\033[1;34mO\033[0m" if Ovar[8] else 8)
        print(f'''\n
         {ZERO} | {st1} | {nd2}
        ---|---|---        
         {rd3} | {th4} | {th5}
        ---|---|---
         {th6} | {th7} | {th8}\n\n''')
       
def checkwin(Xvar, Ovar):
     wins = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
     for win in wins:
         if(sum(Xvar[win[0]], Xvar[win[1]], Xvar[win[2]]) == 3):
               print("\n\nWinner Winner Veggie dinner!!! \n   'X' wins the match!!")
               return 1
         if(sum(Ovar[win[0]], Ovar[win[1]], Ovar[win[2]]) == 3):
               print("\n\nWinner Winner Veggie dinner!!! \n   'O' wins the match!!")
               return 0
     return -1

def checkdraw(Xvar, Ovar):
   # print(sum(Xvar + Ovar))
    if(sum(Xvar + Ovar) == 9):
        print("\n     \033[33mMatch Over - Draw\033[34m !!!\033[0m")
        exit()
print(f"Wlc To tic tac toe game!!")
Xvar = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Ovar = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#nvar = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# 1 is for X and 0 is for O
turn = random.choice([0, 1])
printBoard(Xvar, Ovar)
#print(f"{Xvar = }\n{Ovar = }")
while(True):
        try:
            if(turn == 1):
                print("      X's turn\n")
                value = int(input("Value for X's place : "))
                Xvar[value] = 1
                shell("clear")
                printBoard(Xvar, Ovar)
          #print(f"{Xvar = }\n{Ovar = }")
          
            else:
                print("      O's turn\n")
                value = int(input("Value for O's place : "))
                Ovar[value] = 1
                shell("clear")
                printBoard(Xvar, Ovar)
         #print(f"{Xvar = }\n{Ovar = }")
            def sum(a, b, c):
                return a + b + c 
            cwin = checkwin(Xvar, Ovar)
            if(cwin != -1):
                print("\n          Match Over")
                break;
            del sum
            checkdraw(Xvar, Ovar)
            turn = 1 - turn
        except Exception as e:
           if(RuntimeError or TypeError or NameError):
               print(f"   \033[1;31mERROR \033[0m :{e}")
               break;