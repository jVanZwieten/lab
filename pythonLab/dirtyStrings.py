# Using the existing script dirty_strings.py, implement the function named cleanup(). This function accepts one string as input and returns a copy of the string with whitespace removed from the beginning and the end, and all upper case letters changed to lower case. The code to loop over a list of "dirty" strings and call the function is already in place. All you have to do is remove the pass statement and put your code in the cleanup() function.

DIRTY_STRINGS = [
    "  mud   ",
    "grime  ",
    "   filth    ",
    "     messy messy     ",
    "DIRT	",
    "       FILTH and grime    ",
    "Dirt",
    "   Filth,    dirt, grime,    grime, grime, filth, and mud      ",
]


def main():
    for old_string in DIRTY_STRINGS:
        new_string = cleanup(old_string)
        print(f"Before: >{old_string}<\nAfter:  >{new_string}<\n")


def cleanup(s):
    return ' '.join(element.strip().lower() for element in s.split(','))


main()
