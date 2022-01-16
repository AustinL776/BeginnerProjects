import random


def game():
    user = input("Rock, Paper, Scissors, Go... 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return " It's a Tie"
    # r > s, s > p, and p > r
    if is_win(user, computer):
        return "You Won!"

    return 'You Lost!!!'


def is_win(user, computer):
    # return true if player wins
    # r > s, s > p, and p > r

    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
            or (user == 'p' and computer == 'r'):
        return True


print(game())
