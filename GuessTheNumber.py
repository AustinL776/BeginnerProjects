# This is to demonstrate knowledge of loops and how to use them in writing python programs

import random


def people_guess(t):
    random_number = random.randint(1, t)
    people_guess = 0
    while people_guess != random_number:
        people_guess = int(input(f"Aye man, guess which number I'm thinking between 1 and {t}: "))
        if people_guess < random_number:
            print("Bruh, that number is like watching Tony Snell's stat line!!! Try guessing a bigger number.")
        elif people_guess > random_number:
            print("Man, you guessed like you was high like Snoop Dog! This time try guessing lower.")

    print(f"Aye!!! you guessed the number that I was thinking of, which just happened to be {random_number}. That's what"
          f" I'm gonna CashApp you so you can get some McDonald's")


def computer_guess(t):
    low = 1
    high = t
    feedback = ''
    while feedback != 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low  # I could put this as high because in this instance low = high
        feedback = input(f"So, now it's my turn to guess a number. is the number {computer_guess} the number you were "
                         f"thinking of, or am I wrong? Let me know with the letters (L) for too low, (H) for too high, or"
                         f"(C) for correct, since I'm still a computer bruh").lower()
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1


    print(f"Ayee!!! Me, a computer, guessed the the number that you were thinking of which just happened to be "
          f"{computer_guess}. I'm gonna go into sleep mode while trying to process that CashApp from earlier")



people_guess(10)
computer_guess(100)