# Bulls and cows game

import random
import sys


def generate_random():
    """generate random number with number of digits equal to
    the given length (or default to 3), determine a max number of rounds
    equal to 2^length + length"""

    try:
        x = sys.argv[1]
    except:
        x = '3'
    max_round = (2**int(x)) + int(x)
    random_concat = ""
    for n in range(0, int(x)):
        random_number = str(random.randint(0, 9))
        random_concat = random_concat + random_number
    return random_concat, x, max_round

def guess_number():
    """prompt user to type in a guess and provide feedback:
    matching digit in correct position = bull
    matching digit in wrong position = cow"""
    
    random_concat, x, max_round = generate_random()
    print("Let's play the bulls and cows game. You have {} guesses".format(max_round))
    counter = 1
    while counter <= max_round:
        if counter == 1:
            user_input = input("Guess a {}-digit number: ".format(x))
        else:
            user_input = input("Try again: ")
        try:
            int(user_input)
        except:
            print("Invalid input.", end=" ")
            if counter == max_round:
                print("Sorry. You did not guess the number in {} tries. "
                          "The correct number is {}.".format(max_round, random_concat))
                break   
            counter += 1
            continue
        if len(user_input) != int(x):
            print("Invalid input.", end=" ")
            if counter == max_round:
                print("Sorry. You did not guess the number in {} tries. "
                          "The correct number is {}.".format(max_round, random_concat))
                break                
            counter += 1
            continue
        cows_counter = 0
        bulls_counter = 0
        random_cows = random_concat
        for n in range(0, int(x)):
            if user_input[n] == random_concat[n]:
                bulls_counter += 1
            elif user_input[n] in random_cows:
                cows_counter += 1
                pos = random_cows.index(user_input[n])
                random_cows = random_cows[:pos] + random_cows[(pos+1):]
        if bulls_counter == int(x):
            print("Congratulations. You guessed the correct number in {} tries.".format(counter))
            return
        else:
            if counter == max_round:
                    print("Sorry. You did not guess the number in {} tries. "
                          "The correct number is {}.".format(max_round, random_concat))
                    break
            else:
                print("{} bull(s), {} cow(s).".format(bulls_counter, cows_counter), end=" ")
                counter += 1

#########################################################################
def main():

    guess_number()

if __name__ == '__main__':
    main()