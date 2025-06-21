# start the game 
# Ask the user to choose her move (R , P , S)
# pc choose move randomly
# if pc == user -> Tie 
# (Player == paper and pc  == rock) 
# or (player == rock and pc scissors) 
# or (player == scissors and pc paper) 
## You win / user won
# any other case 
## pc won / You lose 

import random

print("+===================================================================================+")
name =input("Enter Your Name : \n ")
print("+===================================================================================+")
print("Hi! " + name)
print("Welcome In Rock , Paper , scissors Game")
print("+===================================================================================+")

user = input("what's your choice? 'r' for rock , 'p' for paper , and 's' for scissors  \n")
pc = random.choice(['r','p','s'])

print("User Played: " + user)
print("Pc Played: " + pc)

if user == pc :
    print("It's a tie!")
    print("Try Agian")
elif (user == 'p' and pc  == 'r') or (user == 'r' and pc =='s') or (user == 's' and pc == 'p'):
    print("You win " + name)
else:
    print("Pc win  / You Lose! " + name)

print("+===================================================================================+")
