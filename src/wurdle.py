#!/usr/bin/env python3.10

from colorama import Fore
from random import choice
import pyfiglet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tries", type=int, help="change the amount of tries you can have (from 1 to 20)")
args = parser.parse_args()

maxtries = 6
if args.tries:
    if args.tries > 20:
        maxtries = 20
    else:
        maxtries = args.tries

words = ["abbey", "abode", "abyss", "actor", "amuse", "ashen", "baker", "baked", "burnt", "bushy", "chump", "champ", "carol", "chant", "choir", "chuck", "cloud", "curvy", "dealt", "digit", "ditto", "dried", "dwelt", "exact", "eliza", 
         "faced", "fairy", "fiend", "flair", "fluid", "funny", "glove", "grave", "great", "guilt", "guild", "heart", "human", "humor", "ideal", "items", "joint", "jokes", "juicy", "knife", "knock", "labor", "label", "loads", "lunar", 
         "lying", "macro", "match", "meats", "medal", "merge", "music", "named", "ninja", "notes", "nurse", "oasis", "orbit", "order", "outer", "pages", "piano", "pedal", "pixel", "pupil", "query", "quote", "radio", "reign", "rider",
         "rigid", "river", "robot", "sauce", "scope", "seeds", "sense", "shark", "skirt", "skull", "stark", "strip", "table", "taste", "theft", "theme", "torch", "trial", "tribe", "types", "ultra", "unity", "usual", "users", "vague",
         "valid", "viral", "virus", "voter", "wagon", "wages", "waste", "whale", "wheat", "white", "woman", "wrong", "wrote", "yacht", "young", "zones", "zeros"]

word = choice(words)
tries = 0
guessed = False
picked = []

while not guessed and tries < maxtries:
    if len(picked) != 0:
        print("You have guessed: ", end="")
        for i in range(len(picked)):
            print(picked[i], end=", ")
        print()

    guess = input("Enter guess (5 characters): ")
    printed = ""
    if len(guess) != 5:
        print("Guess is not 5 characters!")
        continue

    for i in range(len(guess)):
        if guess[i] == word[i]:
            printed += Fore.GREEN + guess[i]
        elif guess[i] in word:
            printed += Fore.YELLOW + guess[i]
        else:
            printed += Fore.RESET + guess[i]
            if guess[i] not in picked:
                picked.append(guess[i])

    print(printed + Fore.RESET)
    
    if guess == word:
        guessed = True

    tries += 1

if guessed:
    print(f"You got the word in {tries} tries! The word was " + Fore.GREEN)
    print(pyfiglet.figlet_format(word, font="6x10"))
else:
    print("You didn't get the word. The word was " + Fore.GREEN + word)
