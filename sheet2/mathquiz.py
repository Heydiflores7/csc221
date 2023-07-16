# Math Quiz

from random import randint
score = 0 
for x in range(10):
    
    numb1 = randint(1, 10)
    numb2 = randint(1, 10)
    product = numb1 * numb2
    question = "What is " + str(numb1) + " times " + str(numb2) + "?"
    
    answer = int(input(question)) 
    if answer == product:
        print("Great job, you got it right!")
        score +=1 
    else:
        print("Incorrect, try again!")
    
if question == 10:
        print("End quiz")
        print("I asked you 10 questions. You got " + str(score) + "of them right.")

import time
time.strftime('%A, %d %B %Y, at %I:%M%p', time.localtime(time.time()))
'Wednesday, 5 July 2023, at 2:40AM'
time.sleep(1)
    


