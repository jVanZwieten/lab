
import sys
import textwrap
import math


def isWeird(n):
    return n % 2 > 0 or 6 <= n <= 20


def testIsWeird():
    odds = [1, 3, 25, 99]
    withinWeirdRangeEven = [7, 12, 18]
    withoutWeirdRangeEven = [4, 24, 26, 98]

    oddsResults = list(map(lambda x: isWeird(x), odds))
    withinWeirdRangeEvenResults = list(
        map(lambda x: isWeird(x), withinWeirdRangeEven))
    withoutWeirdRangeEvenResults = list(
        map(lambda x: isWeird(x), withoutWeirdRangeEven))


def printSumDifferenceProduct(x, y):
    print(x+y)
    print(x-y)
    print(x*y)


def printBothDivisions(x, y):
    print(x//y)
    print(x/y)


def printSquaresLessThan(n):
    i = 0
    while i < n:
        print(i**2)
        i += 1


def is_leap(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


def incrementingMassiveNumber(n):
    i = 1
    sum = 0
    while i <= n:
        sum *= 10**(1+math.floor(math.log10(i)))
        sum += i
        i += 1
    return sum


def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


def count_substring(string, sub_string):
    i = -1
    count = 0
    while True:
        i = string.find(sub_string, i+1)
        if i == -1:
            break
        count += 1
    return count


def hasAny(input,  predicate):
    return any(predicate(letter) for letter in input)


HACKERRANK_LOGO_CHARACTER = 'H'
BODY_LEFT_PADDING = 2
LEG_LENGTH = 6


def hackerrankLogo(thickness):
    logo = generateTopHat(HACKERRANK_LOGO_CHARACTER, thickness)
    return logo


def generateTopHat(logoCharacter, thickness):
    for i in range(thickness):
        line = logoCharacter*(1+2*i)
        line = line.center(thickness*2-1, " ")
        yield line


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


def generateVectorsInRangeThatDontSumTo(x, y, z, noSum):
    return [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i, j, k]) != noSum]


def runnerUp(scores):
    return sorted(set(scores))[-2]


# The first line contains n. The second line contains an array A[] of n integers each separated by a space.
# Print the runner-up score.
if __name__ == '__main__':
    input()
    scores = map(int, input().split(' '))
    print(runnerUp(scores))
