from dataset_apps_decode_gen_input_run.dsl_impl_copy_to_run import *



def max_score(t: int, test_cases: list) -> list:
    res = []

    for i in range(t):
        n, k = test_cases[i][0]
        s = test_cases[i][1]

        # Count the number of consecutive wins
        consecutive_wins = 0
        for j in range(n):
            if s[j] == "W":
                consecutive_wins += 1
            else:
                break

        # Handle edge cases where k is larger than the number of wins
        if k >= consecutive_wins:
            res.append(2 * consecutive_wins - 1 + min(k - consecutive_wins, n - consecutive_wins))
            continue

        # Initialize variables
        score = 0
        wins = 0

        # Calculate the initial score and wins
        for j in range(n):
            if s[j] == "W":
                if j > 0 and s[j - 1] == "W":
                    score += 2
                else:
                    score += 1
                wins += 1

        # Cheat to maximize the score
        for j in range(n):
            if s[j] == "L":
                if j == 0:
                    if k > 0:
                        score += 2
                        k -= 1
                elif j > 0 and s[j - 1] == "W":
                    if k > 0:
                        score += 2
                        k -= 1
                else:
                    if k > 0:
                        score += 1
                        k -= 1

        res.append(score)

    return res

