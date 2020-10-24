#!/usr/bin/python3
import string, random, time

# Define important global variables
TARGET = ''
TARGET_LEN = 0
LETTERS = string.ascii_uppercase + ' ' + string.punctuation
GENERATIONS = 100
GENERATION_POPULATION = 100

allGenerations = []

# Define the characteristics for the best string of a generation
bestString = {
    'string': '',
    'score': 0,
    'base_for_new_generations': ''
    }

# Function to create a single random string of
# The target length -
def randomString(target_len):
    # Return nothing joined by random letters within the target length
    return ''.join(random.choice(LETTERS) for _ in range(target_len))

# Create 100 random strings
def createInitialStrings():
    # Append to a global list 100 random strings of TARGET_LEN
    allGenerations.append([randomString(TARGET_LEN) for _ in range(GENERATION_POPULATION)])

# Use the best of the previous generation to be used for 
# The creation of the new generation
def constructNewBaseForGeneration(best):
    base_new_generation = ''
    for i in range(TARGET_LEN):
        if TARGET[i] == best[i]:
            base_new_generation = base_new_generation + best[i]
        else:
            # If the character is not the same insert an *
            base_new_generation = base_new_generation + '*'
    # Set the new base
    bestString['base_for_new_generation'] = base_new_generation

# Swap a non matched character for a new character
def switchChar(string, index, char):
    return string[:index] + char + string[index + 1:]

# Replace all * with a random character
def replaceNonMatchesWithRandomChar():
    # Create a temporary string based on our previous generation
    tempString = bestString['base_for_new_generation']
    # For each letter within each string
    for i, letter in enumerate(tempString):
        if letter == '*':
            tempString = switchChar(tempString, i, random.choice(LETTERS))
    return tempString

# Create a new generation of strings based on the best string
# From the previous generation
def createNewGeneration():
    # Create a new base of random characters
    constructNewBaseForGeneration(bestString['string'])
    # Append the new 100 strings to our all generations list
    allGenerations.append([replaceNonMatchesWithRandomChar() for _ in range(GENERATION_POPULATION)])

# Update the new best string as well as the score
def updateBestString(string, score):
    bestString['string'] = string
    bestString['score'] = score


# Score the string against the target
def scoreString(string):
    score = 0
    for i in range(TARGET_LEN):
        if TARGET[i] == string[i]:
            score = score + 1
    return score

# Check to see the string which is closest to our
# target string
def checkMatch():
    latest_generation = allGenerations[-1]
    # For each string in the list
    for string in latest_generation:
        # Score the string (determine how similar it is to target)
        score = scoreString(string)
        # Determine which of the strings is the closest
        if score > bestString['score']:
            # Set that string as the best string, with its score
            updateBestString(string, score)

# Print the string which most closely resembles the target string
def printBestString():
    print('Generation: ' + str(len(allGenerations)) + ' | Current best string: [ ' + bestString['string'] + ' ]')

# Function to represent a monkey typing on a typewritter
def monkeys(target):
    # Declare globals
    global TARGET
    TARGET = target 
    global TARGET_LEN
    TARGET_LEN = len(target)
    # Create the first randomized string
    createInitialStrings()
    # Check to see if the first string matches our target
    checkMatch()
    printBestString()
    time.sleep(1)
    # Go through 100 possible generation
    for _ in range(GENERATIONS):
        if bestString['string'] == TARGET:
            print('Script completed. Matched in ' + str(len(allGenerations)) + ' generations')
            return ''
        # If the first string is not our target, we have to refine this string
        # But still start a new generation of strings
        createNewGeneration()
        # Check to see how close this new generation is to the target
        checkMatch()
        # Print the best of the generation
        printBestString()
        time.sleep(1)

# Execute the primary function for the program
if __name__ == '__main__':
    monkeys(input('Enter a string: ').upper())
