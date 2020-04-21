"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can 
      totally do that by clicking: File -> Download Workspace in the file 
      menu after you fork the snapshot of this workspace.

"""

import os
import random


# These are DEFAULT values
RANGE_START = 1
RANGE_STOP = 100

def display_title_banner() -> None:
    title_banner = "\n\t\t\tGUESS THE NUMBER!" + \
                   "\n\t\t    A Game of Informed Choice\n"
    print(title_banner)


def display_help() -> None:
    help_msg = "(Press 'Q' to quit at anytime.)"
    print(help_msg)


def display_welcome_message() -> str:
    welcome_msg = "Welcome to 'Guess a Number!', the game where you try " + \
                  "to guess which number I'm artificially thinking of!"
    name_prompt = "\nBefore we begin, would you please tell me your name? >  "
    print(welcome_msg)
    display_help()
    return input(name_prompt)


def display_program_exit(name: str = "") -> None:
    name_part = "" if len(name) == 0 else (", " + name)
    program_exit_msg = f"\nThank you for playing{name_part}!"
    print(program_exit_msg)


def check_for_quit(user_input: str) -> bool:
    return user_input.lower() == "q"


def check_for_yes(user_input: str) -> bool:
    return user_input.lower() == "y"


def verify_quit() -> bool:
    verify_q_prompt = "\nLooks like you entered 'Q'.\n" + \
                      "Did you want to quit? Y/N >  "
    n_msg = "\nOkay, got it! Thanks for confirming!"
    y_msg = "\nYou got it!"

    user_input = input(verify_q_prompt)
    if check_for_yes(user_input):
        print(y_msg)
        return True
    else:
        print(n_msg)
        return False


def wants_to_quit(user_input: str, user_name: str = "") -> bool:
    if check_for_quit(user_input):
        if verify_quit():
            display_program_exit(user_name)
            return True
    
    return False


def prompt_for_guess(user_name: str) -> int:
    guess_prompt = "\nWhat is your guess? >  "
    retry_msg = "Please try again."

    while True:
        user_guess = input(guess_prompt)
        if wants_to_quit(user_guess, user_name):
            return -1

        try:
            user_guess = validate_input_int(user_guess)
        except ValueError as err:
            print("\nINVALID GUESS: ")
            print(err)
        else:
            return user_guess

        print(retry_msg)


def validate_input_int(user_input: str) -> int:
    err_msg_not_an_int = "Please enter a number, unless you want to quit..."
    err_msg_out_bounds = "You must pick a number between " + \
                         f"{RANGE_START} and {RANGE_STOP}."

    try:
        guess = int(user_input)
    except ValueError:
        raise ValueError(err_msg_not_an_int)
    else:
        if guess < RANGE_START or guess > RANGE_STOP:
            raise ValueError(err_msg_out_bounds)
        else:
            return guess


def play_again() -> bool:
    again_prompt = "\nWould you like to play again? Y/N >  "
    n_msg = "\nYou got it!"
    y_msg = "\nExcellent! I'm glad you're enjoying it!"

    user_input = input(again_prompt)
    if check_for_yes(user_input):
        print(y_msg)
        return True
    else:
        print(n_msg)
        return False


def start_game() -> None:
    # Everthing outside of the Outer Game Loop is set once initially, and then
    #   used throughout the two loops.
    display_title_banner()
    # These variables will be used all the way till the games exit, and are 
    #   therefore being set outside of loops
    user_name = display_welcome_message()
    # Checking for the edge case where the User enters 'Q' as a name and not
    #   to quit.
    if wants_to_quit(user_name):
        return
    elif len(user_name) == 0:
        user_name = "Anonymous Jones"
        print(f"\nInto anonymity, eh? I'll call you {user_name}!")
    else:
        print(f"\nThank you, {user_name}!")
    
    while True:
        # This is the Outer Game Loop, it is responsible for resetting the game
        #   if the User would like to play again.
        #x   -   Select the random number
        #x   -   Initialize the Attempts list
        attempts = []
        win_case = random.randint(RANGE_START, RANGE_STOP)
        # For DEBUG only, remove before final
        print(f"The low num is: {RANGE_START}\nThe high num is: {RANGE_STOP}")
        print(f"The win case is: {win_case}")

        while True:
            print("\#-- INSIDE INNER LOOP --\#")
            # This is the INNER GAME LOOP. It will:
            #   -   Let the User know that what the range is
            #   -   Prompt the User for their answer
            #       -   Validate that the User's answer is within range and of
            #           the appropriate type, and raise a ValueError if it 
            #           violates either of those two things.
            #   -   Let the User know if they are too low, too high, or right
            #       on
            #       -   If the User is too high or too low, add guess to 
            #           attempts at list, let them know, and loop 
            #       -   If the User guessed correctly, congratulate them, 
            #           display their attempts and attempt counts, and exit the 
            #           loop
            #   -   Ask the User if the would like to play again
            #       -   If yes, then re-outer-loop
            #       -   If no, then exit-outer-loop
            user_input = prompt_for_guess(user_name)
            # This will check if the User wants to quit
            if user_input == -1:
                return

            attempts.append(user_input)
            if user_input < win_case:
                print(f"\n{user_input} is too low!")
                continue
            elif user_input > win_case:
                print(f"\n{user_input} is too high!")
                continue
            else:
                print(f"\n{user_input} is the winning answer!\nCONGRATULATIONS!")
                print(f"You solved it in {len(attempts)} attempts!")
            
            break

        # AFTER INNER LOOP EXIT: Prompt the User to see if they would like to 
        #   play again
        if play_again():
            continue
        else:
            break

    # AFTER OUTER LOOP EXIT: Point #5 part B, letting the User known when the 
    #   program is exiting 
    display_program_exit(user_name)


    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    x01. Display an intro/welcome message to the player.
    02. Store a random number as the answer/solution.
    03. Continuously prompt the player for a guess.
        a.  If the guess greater than the solution, display to the player 
            "It\'s lower".
        b.  If the guess is less than the solution, display to the player 
            "It\'s higher".
    
    04. Once the guess is correct, stop looping, inform the user they "Got it"
        and show how many attempts it took them to get the correct number.
    05. Let the player know the game is ending, or something that indicates 
        the game is over.
    
    ( You can add more features/enhancements if you\'d like to. )

    EXTRA CREDIT
    ------------------------------------
    01. As a player of the game, my guess should be within the number range. 
        If my guess is outside the guessing range I should be told to try 
        again.
    02. As a player of the game, after I guess correctly I should be 
        prompted if I would like to play again.
    03. As a player of the game, at the start of each game I should be shown 
        the current high score (least amount of points) so that I know what 
        I am supposed to beat.
    04. Every time a new game is started, the random number guess should be 
        changed so players are guessing something new.
    """
    # write your code inside this function.

    #x Display Intro Message and Banner
    #x Display Instructions and Help
    # Prompt for Game Mode: Regular, Custom, Computer Guess
        # Regular: User guesses between 1 and 10
        # Custom: User chooses the range upper limit
        # Computer Guess: User picks a number between 1 and 100
        # Multiples Of: User picks a number, the program generates a list of 
        #               multiples of that number based on 1 - 20, and the 
        #               User has to guess which multiple it is.
    # Store the randomly selected wincase number in a variable
    # Get guess input from the User
        # Validate User input and reloop if received inappropriate response
    # Check against the answer
        # If no the answer
            #Reloop and let them know "Too High!" or "Too Low!"
        # Else
            # Let them know they are correct
    # Display Exit Message
    '''
    OUTER LOOP TODO:
        #   -   What version of the game does the User want to play
        #   -   Populate the ranges
    '''


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
