import random
import time

def choose_difficulty():
    print("Choose Difficulty Level")
    print("1- Easy (1-20)")
    print("2- Medium (1-100)")
    print("3- Hard (1-150)")
    print('Choose (1/2/3)')
    choice = int(input('>'))
    if choice == 1:
        return 20,3
    
    elif choice == 2:
        return 100,5
    
    elif choice == 3:
        return 150,7
    else:
        print("Invalid choice, defaulting to Easy.")
        return 20, 3

def calcScore(timeTaken,attempt):
    maxScore=100
    timePanelty = timeTaken*0.5
    attemptPanelty = (attempt-1)*15
    score = maxScore-timePanelty-attemptPanelty
    return min(max(0, score), maxScore)

def guessingGame():
    upperLimit,attempts = choose_difficulty()
    correct_num = random.randint(1,upperLimit)
    print(f"Guess a number between range 1-{upperLimit}. You have {attempts} attempts.")
    start_time=time.time()

    showHint = int(attempts/2)

    for attempt in range(attempts):
        guess_num = int(input('>'))

        if guess_num < correct_num:
            print('Too Low..')
        elif guess_num > correct_num:
            print('Too High..')
        else:
            end_time=time.time()
            timeTaken = end_time-start_time
            score = calcScore(timeTaken,attempt)
            print(f"Congratulation! You guessed it Right. You took {timeTaken:.2f} seconds")
            print(f'Your Score is {score:.2f}/ 100')
            break
        if attempt == showHint:
            if correct_num%2==0:
                print('==============================')
                print("| Hint |: The number is Even")
                print('==============================')

            else:
                print('==============================')
                print("| Hint |: The number is Odd")
                print('==============================')
    else:
        end_time = time.time()
        timeTaken = end_time-start_time
        print(f'Sorry you have used all your {attempts} attempts. The original number is {correct_num} ')
        print(f'You took {timeTaken:.2f} seconds')

guessingGame()
        
