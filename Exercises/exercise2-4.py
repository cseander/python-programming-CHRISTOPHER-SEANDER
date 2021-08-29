import random as rnd

x, y, answer, score = 0, 0, 0, 0
play_again = ""
keep_playing = True

while keep_playing:
    x = rnd.randint(1, 10)
    y = rnd.randint(1, 10)
    answer = input(f"What is {x} times {y}? ")
    if int(answer) == x * y:
        print("Good work!")
        score += 1
    else:
        print(f"The answer was {x * y}")

    print(f"Your score is {score}")
    play_again = input("Play again? ")
    if play_again == "no":
        print("Thank you for playing!")
        keep_playing  = False

