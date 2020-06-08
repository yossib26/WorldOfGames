from GuessGame import play as play_guess_game
from MemoryGame import play as play_memory_game
from CurrencyRouletteGame import play as play_roulette_game

def welcome(name):
    try:
        if not isinstance(name, str):
            raise IOError
        print("Hello " + name + " and welcome to the World of Games (WoG).")
        print("Here you can find many cool games to play.")
    except IOError:
        print("Please check player name!")


def load_game():
    arr_games = []
    arr_games.append("Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    arr_games.append("Guess Game - guess a number and see if you chose like the computer")
    arr_games.append("Currency Roulette - try and guess the value of a random amount of USD in ILS")
    g_count = 1
    game_win = False

    # print all games
    print("Please choose a game to play:")
    for game in arr_games:
        print(str(g_count) + ". " + game)
        g_count += 1

    # ask user to choose game
    chosen_game = str(input("Choose a game:"))

    while True:
        if chosen_game.isdigit() == True:
            if int(chosen_game) in range(1, 4):
                # check game level
                # ---------------------------------------------------------------------------
                game_level = input("Please choose game difficulty from 1 to 5:")
                while True:
                    if game_level.isdigit() == True:
                        if int(game_level) in range(1, 6):

                            print("Lets play Game " + str(chosen_game) + " Level " + str(game_level) + "...")

                            # run game
                            if int(chosen_game) == 1:
                                game_win = play_memory_game(game_level)
                            elif int(chosen_game) == 2:
                                game_win = play_guess_game(game_level)
                            elif int(chosen_game) == 3:
                                game_win = play_roulette_game(game_level)
                            break

                    print("Level not Exist! Try again.")
                    game_level = input("Please choose game difficulty from 1 to 5:")
                # ---------------------------------------------------------------------------
                break
        print("Game not Exist! Try again.")
        chosen_game = str(input("Choose a game:"))