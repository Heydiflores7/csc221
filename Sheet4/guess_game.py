from random import randint
guesses = 1
number = randint(1, 1000)
print("OK, I've thought of a number between 1 and 1000")
guess= int(input("Take a guess: "))

while guess != number: 
  if guess > number:
    print("That's too high")
    guess = input("Try again")
    guesses = guesses +1

  elif guess < number:
    print("That's too low")
    guess = input("Try again")
    guesses = guesses +1
  else:
    print ("Genius, your guess is right!")

print("You took", guesses, "guesses!")