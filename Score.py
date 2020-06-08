from MainScores import *


def add_score(difficulty = 1):
    current_score = get_current_score()
    # calc points
    point_of_winning = (int(difficulty) * 3) + 5
    current_score = int(current_score) + point_of_winning
    update_current_score(current_score)

    return point_of_winning


def get_current_score():
    try:
        player_scores = 0
        if os.path.isfile(SCORES_FILE_NAME):
            # read file content
            scores_file = open(SCORES_FILE_NAME, "r")
            player_scores = scores_file.readline()
            if not player_scores.isdigit():
                player_scores = 0
            scores_file.close()
        else:
            # create new file
            scores_file = open(SCORES_FILE_NAME, "w")
            scores_file.write(str(player_scores))
            scores_file.close()

        return player_scores

    except IOError:
        print("Error creating scores file ....")
        return BAD_RETURN_CODE


def update_current_score(current_score):
    try:
        # write score to file
        scores_file = open(SCORES_FILE_NAME, "w")
        scores_file.write(str(current_score))
        scores_file.close()
        return True
    except IOError:
        print("Error creating scores file ....")
        return False
