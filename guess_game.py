from random import randint
number = randint(1, 1000)
guess = 0 
while guess != number: 

  guess = int(input("Enter a guess: "))

  if guess > number:
    print("That's too high")
  elif guess < number:
    print("That's too low")
  else:
    print("Genius, your guess is right!")