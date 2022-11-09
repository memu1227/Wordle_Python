#!/usr/bin/env python
# coding: utf-8

# # Python Assignment 1: Wordle

#install colored module
#python3 -m pip install colored

#import libraries
import random
from colored import fg, bg, attr

print("RULES: \n The player has SIX chances to guess a five-letter word")
print()
print("After each guess, the color of the tiles will change to show how close the guess was to the word:")
print("BLUE means that the letter is in the word but in the wrong spot")
print("GREEN means that the letter is in the word and in the correct spot")
print("RED means that the letter is not in the word")
print()


#STEP 1: Read a file that has a list of five-letter words. This is the "words.txt" file included in the assignment
   
path = "/Users/meghamurthy/Documents/NJIT/Data Analytics for Info Sys/words.txt"
lines = []
with open(path) as test:
    lines = test.readlines()
    

#STEP 2: Randomly choose a word as your puzzle 

index = random.randint(1,len(lines))
#print(f"Index of word: {index}")
word_of_day = (lines[index]).upper().strip()
#print(f"{index} = {word_of_day}")

#can comment out to play without knowing... print for testing purposes
print(f"Word of the day: {word_of_day}")


#STEP 3: Prompt the user to enter a five-letter word 
#Check the input against your word and give feedback to the user

#counter
count = 0

while count < 6: 
    color = bg("black") + fg("white")
    user_word = (input(color + "\nPlease guess a five-letter word: ")).upper()
    while len(user_word) != 5:
        user_word = (input("Please guess a five-letter word: ")).upper()
    list_userword = list(user_word)
    #print(list_userword)
    list_randword = list(word_of_day)
    #print(list_randword)
    if list_userword == list_randword:
        color = bg("green") + fg("white")
        print(color + user_word)
        break;
    for i in range(len(list_userword)):
        if list_userword[i] == list_randword[i]:
            color = bg("green") + fg("white")
        elif list_userword[i] in list_randword:
            color = bg("blue") + fg("white")
        else:
            color = bg("red") + fg("white")
        print(color+ list_userword[i], end = " ")
    count += 1

if user_word == word_of_day:
    color = bg("black") + fg("white")
    print(color + "Congrats! You solved today's Wordle!", end = " ")
else:
    color = bg("black") + fg("white")
    print(color + f"\nThe word was: {word_of_day}. \nSorry, try again tomorrow!")








