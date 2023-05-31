from Utils import BAD_RETURN_CODE

POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5


class ScoreManager:
    @staticmethod
    def add_score(difficulty):

        try:
            with open("Scores.txt", "r") as file:
                current_score = int(file.read())
        except FileNotFoundError:
            current_score = 0
        except Exception:
            return BAD_RETURN_CODE

        current_score += POINTS_OF_WINNING(difficulty)

        try:
            with open("Scores.txt", "w") as file:
                file.write(str(current_score))
        except Exception:
            return BAD_RETURN_CODE
