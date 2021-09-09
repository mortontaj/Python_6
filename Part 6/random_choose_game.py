import random

low = 0
max = 100
answer = random.randint(low, max)

guess = int(input("Guess a number between {} and {}: "
      .format(low, max)))

tries = 1
while guess == answer:
    print("Well done! You guessed on first try")
    break

while guess != answer:
    while guess < answer and tries <= 10:
        guess = int(input("Guess higher: "))
        break

    while guess > answer and tries <= 10:
        guess = int(input("Guess lower: "))
        break

    while guess == 0 or tries == 11:
        print("game over. {} was the answer"
              .format(answer))
        break
    tries += 1

while guess == answer and tries != 1:
    print("Correct! You guess in {} attempts."
          .format(tries))
    break
