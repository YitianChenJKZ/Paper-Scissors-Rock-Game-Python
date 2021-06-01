#!/bin/python3
# Yitian Chen. Copyright. All Rights Reserved. 2021
# Instructions: Please click 'Run' and type 's' for Scissors, 'r' for Rock and 'p' for Paper
# 

from random import randint

player = input('Scissors (s) , Rock (r) Or Paper (p) ？')

print(player, 'vs' , end=' ')

chosen = randint(1,3)
#print(chosen)

if chosen == 1:
    computer = 'Rock'

elif chosen == 2:
    computer = 'Paper'

else :
    computer = 'Scissors'

print(computer)

if(player == computer):
    print('Draw！')

elif(player == 'r' and computer == 'Scissors'):
    print('You Won！The computer played Scissors')

elif(player == 'r' and computer == 'Paper'):
    print('You Lost！The computer played Paper')

elif(player == 'p' and computer == 'Rock'):
    print('You Won！The computer played Rock')

elif(player == 'p' and computer == 'Scissors'):
    print('You Lost！The computer played Scissors')

elif(player == 's' and computer == 'Paper'):
    print('You Won！The computer played Paper')

elif(player == 's' and computer == 'Rock'):
    print('You Lost！The computer played Rock')
