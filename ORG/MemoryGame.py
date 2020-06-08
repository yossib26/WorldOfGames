import random
from Score import add_score

MIN_NUM = 1
MAX_NUM = 101

# start play
def play(difficulty):

    game_res = False

    rnd_list = generate_sequence(int(difficulty))
    print(rnd_list)

    usr_list = get_list_from_user(difficulty)
    print("Random List : " + str(rnd_list))
    print("Your List :   " + str(usr_list))

    eq_res = is_list_equal(rnd_list, usr_list)
    if eq_res:
        add_score(difficulty)
        print("*********************  You Won !!!!!!   ********************************")
        game_res = True
    else:
        print("Failed! Try again ...")

    return game_res


# ----------------------------------------------------------------

def generate_sequence(difficulty):

    rnd_list = []
    lst_count = 1

    if isinstance(difficulty, int):
        while lst_count <= int(difficulty):
            rnd_num = random.randint(MIN_NUM, MAX_NUM)
            rnd_list.append(str(rnd_num))
            lst_count += 1

    return rnd_list

# ----------------------------------------------------------------

def get_list_from_user(difficulty):

    usr_list = []
    lst_count = 1

    while lst_count <= int(difficulty):
        usr_num = input("Please enter number between " + str(MIN_NUM) + " to " + str(MAX_NUM) + ":")
        if usr_num.isdigit():
            if int(usr_num) in range(MIN_NUM, MAX_NUM+1):
                usr_list.append(usr_num)
                lst_count += 1
            else:
                print("Number not in range %s - %s..." % (MIN_NUM, MAX_NUM))

    return usr_list

# ----------------------------------------------------------------

def is_list_equal(rnd_list, usr_list):

    if isinstance(rnd_list, list) and isinstance(usr_list, list):
        rnd_list.sort()
        usr_list.sort()
        if rnd_list == usr_list:
            return True

    return False

# ----------------------------------------------------------------

# start game
# print(play(2))
