def guess_animal(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer ) 
score = 0
print("Guess the Animal")
Q1 = input("Which bear lives at the North Pole? ")
guess_animal(Q1, "polar bear")
Q2 = input("Which is the fastest land animal? ")
guess_animal(Q2, "Cheetah")
Q3 = input("Which is the larget animal? ")
guess_animal(Q3, "Blue Whale")
print("Your Score is "+ str(score))