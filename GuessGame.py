import random
# from Score import add_score


# start play
def play(difficulty):
    game_res = False
    secret_number = generate_number(difficulty)
    print("secret_number = " + str(secret_number))
    user_guess = get_guess_from_user(difficulty)
    print("user_guess = " + str(user_guess))
    while True:
        res_compare = compare_results(secret_number, user_guess)
        if res_compare == True:

            # add_score(difficulty)

            print("*********************  You Won !!!!!!   ********************************")
            game_res = True
            break
        else:
            print("Please guess again...")
            user_guess = get_guess_from_user(difficulty)
    return game_res


# check user guess
def compare_results(secret_number, user_guess):
    if int(secret_number) == int(user_guess):
        return True
    else:
        return False


# get input from user
def get_guess_from_user(difficulty):
    while True:
        guess = input("Please enter number between 1 to " + str(difficulty) + ":")
        if guess.isdigit():
            if int(guess) in range(1, int(difficulty) + 1):
                break
            else:
                print("Please enter a number between 1 to " + str(difficulty) + "!")
        else:
            print("Please enter a valid number!")
    return guess


# generate secret number
def generate_number(difficulty):
    try:
        n = random.randint(1, int(difficulty))
    except:
        n = -1
    return n

# ----------------------------------------------------------------
