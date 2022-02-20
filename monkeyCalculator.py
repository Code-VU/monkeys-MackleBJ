def calculateTime():
    
    # This first line is provided for you
    
    # While loop to error check user's input. Continues until y or
    # n entered.
    while True:    
        monkey_one = input("Is the first monkey smiling?:  ")
        if monkey_one != 'y' and monkey_one != 'n':
            print("Please enter y or n.")
            continue
        else:
            break
    
    # While loop to error check user's input. Continues until y or
    # n entered.
    while True:
        monkey_two = input("Is the second monkey smiling?: ")
        if monkey_two != 'y' and monkey_two != 'n':
            print("Please enter y or n.")
            continue
        else:
            break

    if monkey_one == monkey_two:
        print("Uh Oh! We're in trouble!")
    else:
        print("Yay! We're going to have a good day!")
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateTime() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
calculateTime()