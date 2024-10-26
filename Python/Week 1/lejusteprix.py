import random
tour_needed_to_guess = 0
haveToGuessNumber = random.randint(0,100)

print(haveToGuessNumber)

print("guess the number between 1 and 100 ! \n"
      "Please input the number you think is the good one")
guessing = input("what do you think it is ? : ")

guessing = int(guessing)

found = False

while found == False:
    if int(guessing) > int(haveToGuessNumber):
        print("My number is smaller")
        tour_needed_to_guess = tour_needed_to_guess++1
        print(tour_needed_to_guess)
        print("we added 1 to your number of tour")
        guessing = input("what do you think it is ? : ")
    if int(guessing) < int(haveToGuessNumber):
        print("My number is greater than this one")
        tour_needed_to_guess = tour_needed_to_guess++1
        print(tour_needed_to_guess)
        print("we added 1 to your number of tour")
        guessing = input("what do you think it is ? : ")
    if int(guessing)  == int(haveToGuessNumber):
        print("Yay ! \n You find the right number in :", tour_needed_to_guess+1, "tours ! ")
        found = True
    


