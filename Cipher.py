# @File: Cipher.py
# @Author: Robert Randolph
# @Class: COSC 5010-01
# @Assignment: Homework 05 Part 1
# @Due: September 27, 2020
# @Description:
# Asks the user to insert a string
# After sanatizing the string, it computes letter frequency of the given string.
# After which it compares the letter frequency to the letter frequency of the english alphabet
# It outputs any mismatch in frequency > 5%
# @Asuumption: Output freqency is a literal differance of 5, not an actual 5% differance.
# Example: A:8.12% and A:3.11% (These are seperated by 5.01 > 5 | so (A) is printed) - Not using 5% error/differance/space between them. Just calculating differance.

# Imports
import re   # Sanatizing string using regular expressions
import string

# CONSTANTS
LETTERS = list(string.ascii_lowercase)
FREQUENCY = [8.12,1.49,2.71,4.32,12.02, # Letter Frequencyies found here: http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
             2.3,2.03,5.92,7.31,0.1,
             0.69,3.98,2.61,6.95,7.68,
             1.82,0.11,6.02,6.28,9.1,
             2.88,1.11,2.09,0.17,2.11,
             0.07]

# Driver
def main():
    # Init
    letters = dict()    # Number of letters in string

    # Setting count to 0
    for l in LETTERS:
        letters[l] = 0

    # Asking for user to input a string
    value = input('Enter a large string of letters:\n')

    # Sanitising string - and converting to lower case
    value = re.sub('[^A-Za-z]*', '', value)
    value = value.lower()

    # Counting letters
    for c in value:
        letters[c] += 1 # Incrimenting total number of specific letter

    # Calculating letter frequency in string
    n = len(value) # Total number of letters
    for l in letters:
        c = letters[l]
        letters[l] = c/n * 100  # Frequency

    # Comparing frequencies
    print('Missmatching frequencies over 5%:')
    index = 0
    missmatched = False
    for l in letters:
        # Getting frequencies
        F1 = letters[l]
        F2 = FREQUENCY[index]

        # Comparing
        r = abs(F1 - F2)

        # Checking if differance is over 5%
        if r > 5:
            missmatched = True
            print('Letter:',l,'| Calculated:',round(F1,4),'| Origional:',round(F2,4),'| Differance:',round(r,4))

        index += 1
    
    # Checking if any mismatches were found
    if not missmatched:
        print('No missmatching frequencies over 5%:')

# Starting driver
if __name__ == '__main__': main()