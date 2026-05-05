import random

NUM_DIGITS = 3
MAX_GUESSES = 9


def main():
    print(
        """ Bagels, a deductive logic game.
 By Al Sweigart al@inventwithpython.com

 Iam Thinking of a {}-digit number with no repeated digits.
 Try to guess what it is. Here are some clues:

 When I say:    That means:
 Pico           One Digit is correct but in the wrong position.
 Fermi          One Digit is correct but in the right position.
 Bagels         No digit is correct.



 For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.""".format(NUM_DIGITS)
    )

    while True:
        secretNum = getSecretNum()
        print("I have thought of a number")
        print("You have {} guesses to get it".format(MAX_GUESSES))
