from random import randint
print("OK, I've thought of a number between 1 and 1000")
number = randint(1, 1000)
guess = 2
guess= int(input("Take a guess: "))

x = 1
while x < 1000:
    print('x is', x)
    x = x + 6

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