import random
from currency_converter import CurrencyConverter
# from Score import add_score

MIN_NUM = 1
MAX_NUM = 100


# start play
def play(difficulty):

    game_res = False

    c = CurrencyConverter()
    curr_rate = c.convert(1, 'USD', 'ILS')
    rnd_num = random.randint(MIN_NUM, MAX_NUM)

    print("----------  Amount -------------------------------")
    print("Amount = " + str(rnd_num) + "$")
    rnd_amount = round(curr_rate * rnd_num, 2)
    print(str(rnd_amount) + " ILS")

    # gwt interval
    intv = get_money_interval(difficulty, rnd_amount)
    # ----------------------------------------------------
    if len(intv) == 2:
        while True:
            # get user guess
            guess = get_guess_from_user()
            # check value
            if float(guess) >= float(intv[0]) and float(guess) <= float(intv[1]):
                print("You Won! In Interval range...")
                game_res = True
                break
            else:
                print("Wrong Guess = " + str(guess) + " ... Try again ...")
    else:
        print("Unexpected Error....Try Later")
    # ----------------------------------------------------
    return game_res


# ----------------------------------------------------------------
def get_money_interval(difficulty, amount):

    try:
        d = int(difficulty)
        t = amount
        intv = (t - (5 - d), t + (5 - d))
        print("iInterval = " + str(intv))
        return intv
    except:
        return -1


# ----------------------------------------------------------------
def get_guess_from_user():
    guess = -1
    while True:
        guess = input("Please enter your ILS Amount guess:")
        if is_number(guess):
            guess = float(guess)
            if isinstance(guess, float):
                break
        else:
            print("Please enter a valid number!")
    return guess


# ----------------------------------------------------------------
# check string if number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# ----------------------------------------------------------------
