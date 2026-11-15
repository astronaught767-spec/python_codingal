import random

secret = random.randint(1, 50)
max_attempts = 5
count=0
guess=0

print("=" * 42)
print("NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

while count < max_attempts and guess != secret:
    guess = int(input("Your guess: "))
    count += 1

    if guess == secret:
        print("correct you have it in", count, "attempts")

    elif guess > secret:
        diff = guess - secret
    else:
        diff = secret - guess

    if diff>= 20:
        print("Ice cold you are way off!")
    elif diff >= 10:
        print("Cold you are not close!")
    elif diff >= 5:
        print("Warm you are getting close!")
    else:
        print("Hot you are very close!")

    remaining = max_attempts - count

    
    if remaining > 0:
        print("Lives left:", end=" ")
        for life in range(remaining):
            print("❤️", end=" ")
        print()

if guess != secret:
    print("Game over u used all ur attempts")
    print("The secret number was", secret)
    