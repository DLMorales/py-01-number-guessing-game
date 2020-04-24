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
LINE_LENGTH = 80
RANGE_START = 1
RANGE_STOP = 100


# Global Variables
attempts = []
attempt_low = RANGE_STOP - RANGE_START
attempt_high = 0
games_won = 0


def reset_attempts() -> None:
    global attempts
    attempts = []


def reset_globals() -> None:
    global RANGE_START
    global RANGE_STOP
    global attempts
    global attempt_low
    global attempt_high
    
    attempts = []
    attempt_low = RANGE_STOP - RANGE_START
    attempt_high = 0
    games_won = 0


def display_title_banner() -> None: #01
    _ = os.system("clear")
    title = "GUESS THE NUMBER!"
    subtitle = "A Game of Informed Choice"

    print_divider("*")
    print()
    print(f"{title:^{LINE_LENGTH}}")
    print(f"{subtitle:^{LINE_LENGTH}}")
    display_help()
    print()
    print_divider("*")
    display_stats()
    print_divider("-")


def print_divider(character: str) -> None: #02
    global LINE_LENGTH
    print(character * LINE_LENGTH)


def plural_s(count: int) -> str:
    return "s" if count > 1 else ""


def display_stats() -> None:
    global attempt_low
    global attempt_high
    attempts_str = attempts_list_to_string()
    low_and_high_str = f"LEAST TRIES: {attempt_low}  MOST TRIES: {attempt_high}"
    stat_str = f"Least Tries: {attempt_low} | " + \
               f"Most Tries: {attempt_high} | " + \
               f"Wins: {games_won} | " + \
               attempts_str
    print(stat_str)


def display_help() -> None: #03
    help_msg = "(Enter 'Q' at anytime to quit)"
    print(f"{help_msg:^{LINE_LENGTH}}")


def display_welcome_message() -> str:   #04
    welcome_msg = "\nWelcome to 'Guess a Number!', the game where you try " + \
                  "to guess which number I'm " + \
                  f"\nartificially thinking of between {RANGE_START} and " + \
                  f"{RANGE_STOP}!"
    name_prompt = "\nBefore we begin, would you please tell me your name? >  "
    print(f"{welcome_msg:<{LINE_LENGTH}}")
    return input(name_prompt)


def display_program_exit(name: str = "") -> None: #05
    name_part = "" if len(name) == 0 else (", " + name)
    program_exit_msg = f"\nThank you for playing{name_part}!\n"
    print(program_exit_msg)
    print_divider("=")
    print()


def attempts_list_to_string() -> str:
    # https://stackoverflow.com/questions/3590165/join-a-list-of-items-with-different-types-as-string-in-python
    global attempts
    attempts_count = len(attempts)
    s = f"Guesses[{attempts_count}]: " # 's' stands for 'string'
    d = ", "         # 'd' stands for 'delimiter'
    e = "..., "    # 'e' stands for 'ellipsis'

    if attempts_count > 5:
        s = s + e + d.join(str(x) for x in attempts[-5:])
    else:
        s = s + d.join(str(x) for x in attempts)
    
    return s


def check_for_quit(user_input: str) -> bool: #07
    return user_input.lower() == "q"


def check_for_yes(user_input: str) -> bool: #08
    return user_input.lower() == "y"


def verify_quit() -> bool: #09
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


def wants_to_quit(user_input: str, user_name: str = "") -> bool: #10
    if check_for_quit(user_input):
        if verify_quit():
            display_program_exit(user_name)
            return True
    
    return False


def prompt_for_guess(user_name: str) -> int: #11
    guess_prompt = "\nWhat's your guess between " + \
                  f"{RANGE_START} and {RANGE_STOP}? >  "
    retry_msg = "\nPlease try again."

    while True:
        user_guess = input(guess_prompt)
        if wants_to_quit(user_guess, user_name):
            return -1

        try:
            user_guess = validate_input_int(user_guess)
        except ValueError as err:
            print("\nINVALID GUESS: ")
            print("--------------")
            print(err)
        else:
            return user_guess

        print(retry_msg)


def validate_input_int(user_input: str) -> int: #12
    err_msg_not_an_int = f"'{user_input}' is not a number...\n" + \
                          "\t...Please enter a number...\n" + \
                          "\t\t...unless you WANT to quit..."
    err_msg_out_bounds = "{user_input} isn't a number between " + \
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


def play_again() -> bool: #13
    again_prompt = "\nWould you like to play again? Y/N >  "
    n_msg = "\nYou got it!"
    y_msg = "\nExcellent! I'm glad you're enjoying it!"

    user_input = input(again_prompt)
    if check_for_yes(user_input):
        reset_attempts()
        display_title_banner()
        print(y_msg)
        return True
    else:
        print(n_msg)
        return False


def start_game() -> None:
    global attempts
    global attempt_low
    global attempt_high
    global games_won

    display_title_banner()
    user_name = display_welcome_message()
    
    display_title_banner()
    if wants_to_quit(user_name):
        reset_globals()
        return
    elif len(user_name) == 0:
        user_name = "Anonymous Jones"
        print(f"\nInto anonymity, eh? I'll call you {user_name}!")
    else:
        print(f"\nThank you, {user_name}!")
    
    while True:
        win_case = random.randint(RANGE_START, RANGE_STOP)
        #DEBUG: print(f"The win case is: {win_case}")

        while True:
            user_input = prompt_for_guess(user_name)

            if user_input == -1:
                return

            attempts.append(user_input)
            display_title_banner()
            if user_input < win_case:
                print(f"\n{user_input} is too low!")
                continue
            elif user_input > win_case:
                print(f"\n{user_input} is too high!")
                continue
            else:
                games_won += 1
                final_attempt_count = len(attempts)
                s = plural_s(final_attempt_count)
                if attempt_low > final_attempt_count:
                    attempt_low = final_attempt_count

                if attempt_high < final_attempt_count:
                    attempt_high = final_attempt_count

                display_title_banner()

                print(f"\nCONGRATULATIONS, {user_name.upper()}!!!")
                print(f"\n{user_input} is the winning guess!")
                print(f"You solved it in {final_attempt_count} attempt{s}!")
            
            break

        if play_again():
            continue
        else:
            break

    display_program_exit(user_name)
    reset_globals()


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
