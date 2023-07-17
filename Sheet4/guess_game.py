from random import randint
number = randint(1, 1000)
guess = 1
guess= int(input("Enter a guess: "))

while guess != number: 
  if guess > number:
    print("That's too high")
    guess = guess +1
  elif guess < number:
    print("That's too low")
    guess = guess +1
  else: 
    print("Genius, your guess is right!")

print("You took", guess, "guesses!")