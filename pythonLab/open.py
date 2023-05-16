# with automatically saves and closes the resource at the end of the suite
# with open(r'C:\Users\e442179\Desktop\pyCourse\mary.txt', 'r') as mary:

import sys
from statistics import mean

DATA_DIRECTORY = r'C:\Users\e442179\Desktop\pyCourse'
TEST_SCORES_FILENAME = 'testScores.dat'
PASSWORDS_FILENAME = 'passwords'
FRUIT1_FILENAME = 'fruit1.txt'
FRUIT2_FILENAME = 'fruit2.txt'


def readLineOneAtATime(textIoWrapper):
    poem = ""
    while line := textIoWrapper.readline():
        poem += line
    return poem


def readLines(textIoWrapper):
    lines = textIoWrapper.readLines()
    poem = lines.join('')
    return poem


def readAsData(textIoWrapper):
    data = textIoWrapper.read()
    return data


def readWithFor(textIoWrapper):
    poem = ""
    for line in textIoWrapper:
        poem += line
    return poem

# Write a program to display each line of a file preceded by the line number. Allow your program to process one or more files specified on the command line. Be sure to reset the line number for each file.


def printEachLineOfFileFromCommandArgsPreceededByLineNumber():
    filePathsToRead = sys.argv[1:]
    finalTexts = generateFilesWithLineNumbers(filePathsToRead)
    for fileText in finalTexts:
        print(fileText)


def generateFilesWithLineNumbers(filePathsToRead):
    for filePath in filePathsToRead:
        yield generateFileWithLineNumbers(filePath)


def generateFileWithLineNumbers(filePath):
    finalText = ""
    with open(filePath) as file:
        i = 0
        for line in file:
            finalText += f'{i} {line}'
            i += 1
    return finalText


def readAndPrintTestScores(dataFilePath):
    ''' A class of students has taken a test. Their scores have been stored in testscores.dat. Write a program named scores.py to read in the data (read it into a dictionary where the keys are the student names and the values are the test scores). Print out the student names, one per line, sorted, and with the numeric score and letter grade. After printing all the scores, print the average score.

    Args:
        dataFilePath (_type_): file path to test scores
    '''
    studentScores = {}

    with open(dataFilePath) as dataFile:
        for record in dataFile:
            student, score = record.split(':')
            studentScores[student] = int(score)

    for record in sorted(studentScores.items()):
        print(record[0], record[1], getLetterGrade(record[1]))

    print('class average:', mean(studentScores.values()))


def getLetterGrade(score):
    return 'A' if score >= 90 else \
        'B' if score >= 80 else \
        'C' if score >= 70 else \
        'D' if score >= 60 else \
        'F'

# Using the file named passwd, write a program to count the number of users using each shell. To do this, read passwd one line at a time. Split each line into its seven (colon-delimited) fields. The shell is the last field. For each entry, add one to the dictionary element whose key is the shell. When finished reading the password file, loop through the keys of the dictionary, printing out the shell and the count.


def readCountAndPrintShellsFromPasswords(dataFilePath):
    with open(dataFilePath) as dataFile:
        data = [record.removesuffix('\n').split(':')
                for record in dataFile.readlines()]
    shellCounts = {datum[-1]: 0 for datum in data}
    for datum in data:
        shellCounts[datum[-1]] += 1
    for shellCount in shellCounts.items():
        print(shellCount)


# Using sets, compute which fruits are in both fruit1.txt and fruit2.txt. To do this, read the files into sets (the files contain one fruit per line) and find the intersection of the sets.
def readAndGetCommonEntries(firstFilePath, secondFilePath):
    with open(firstFilePath) as firstFile:
        set1 = extractSetFromSimpleData(firstFile)
    with open(secondFilePath) as secondFile:
        set2 = extractSetFromSimpleData(secondFile)
    return set1.intersection(set2)


def extractSetFromSimpleData(dataFile):
    return set(record.removesuffix('\n') for record in dataFile.readlines())


# print(readAndGetCommonEntries(f'{DATA_DIRECTORY}\{FRUIT1}', f'{DATA_DIRECTORY}\{FRUIT2}'))
printEachLineOfFileFromCommandArgsPreceededByLineNumber()
