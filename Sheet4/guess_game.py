from random import randint
guesses = 1
number = randint(1, 1000)
print("OK, I've thought of a number between 1 and 1000")
guess= int(input("Take a guess: "))

while guess != number: 
   if guess > number:
    print("That's too high")
    guess = int(input("Try again: "))
    guesses = guesses +1
   elif guess < number:
    print("That's too low")
    guess = int(input("Try again: "))
    guesses = guesses +1
   if number == guess:
    print("Genius, your guess is right!")
    print("You took", guesses, "guesses!")


from gasp.utils import read_yesorno
if read_yesorno('Would you like to play another game?: '):
  print ("I know you like it, but it's over.") 
else:
  print ("OK, bye.")