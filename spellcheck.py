# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Main Menu
    displayMenu = True
    while displayMenu:
        print("\n1. Spell Check A Word (Linear)")
        print("2. Spell check a Word (Binary)")
        print("3. Spell Check Alice in Wonderland (Linear Search)")
        print("4. Spell Check Alice in Wonderland (Binary Search)")
        print("5. Exit")
        option = str(input("Select option 1-5: "))

        if option == "1":
            usrInput = input("Please enter a word: ")
            usrInput = usrInput.lower()
            startTimer = time.time()
            verify = linearSearch(dictionary, usrInput)
            endTimer = time.time()
            if verify == -1:
                print(usrInput + " is NOT IN the dictionary")
                print(f"{endTimer - startTimer}seconds")
            else:
                print(usrInput + f" is in the dictionary at position {verify}")
                print(f"{endTimer - startTimer} seconds")

        elif option == "2":
            usrInput = input("Please enter a word: ")
            usrInput = usrInput.lower()
            startTimer = time.time()
            verify = binarySearch(dictionary, usrInput)
            endTimer = time.time()
            if verify == -1:
                print(usrInput + " is NOT IN the dictionary")
                print(f"{endTimer - startTimer}seconds")
            else:
                print(usrInput + f" is in the dictionary at position {verify}")
                print(f"{endTimer - startTimer} seconds\n")

        elif option == "3":
            count = 0
            startTimer = time.time()
            for i in range(len(aliceWords)):
                verify = linearSearch(dictionary, aliceWords[i])
                if verify == -1:
                    count += 1
            endTimer = time.time()
            print(f"Number of words not found in dictionary: {count}")
            print(f"{endTimer - startTimer} seconds")

        elif option == "4":
            count = 0
            startTimer = time.time()
            for i in range(len(aliceWords)):
                verify = binarySearch(dictionary, aliceWords[i])
                if verify == -1:
                    count += 1
            endTimer = time.time()
            print(f"Number of words not found in dictionary: {count}")
            print(f"{endTimer - startTimer} seconds")

        elif option == "5":
            displayMenu = False
            print("Bye")


# end main()

# Helper Functions

def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1


def binarySearch(anArray, item):
    low = 0
    high = len(anArray) - 1

    # find average for low index
    while low <= high:
        middleIndex = (low + high) // 2

        if item == anArray[middleIndex]:
            return middleIndex
        elif item < anArray[middleIndex]:
            high = (-1 + middleIndex)
        else:
            low = (1 + middleIndex)

    return -1


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)


# end loadWordsFromFile()


# Call main() to begin program
print(main())
