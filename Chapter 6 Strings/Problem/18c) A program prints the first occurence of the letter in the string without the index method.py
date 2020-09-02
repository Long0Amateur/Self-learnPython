# A program that asks the user for a string and a letter
# prints out the index of the first occurrence of the letter in the string.
# If the letter is not in the string, the program should say so
# without the use of index method

# Visit:
# https://stackoverflow.com/questions/3221891/how-can-i-find-the-first-occurrence-of-a-sub-string-in-a-python-string


def find_index(string,letter):

    for i in range(len(string) - len(letter)+1):
        if string[i:i+len(letter)] == letter:
            return i
    return 'Not Found'

string = input('Enter a string:')
letter = input('Enter a letter of the string you would like to find:')

print(find_index(string, letter))

print(string.index(letter))


