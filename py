    
guess_number = False
guess = 0
guess_limit = 0


number  = random.randint(1, 100)

def play_game():
    level = input("Do you want to play 'hard' or 'easy' level? \n")
    if level == 'hard':
        guess_limit= 2
    else:
        guess_limit= 7

        
    while guess_number != True:
        guess = int(input("Guess a number between 1 to 100 \n"))
        
        if guess < number:
            guess_limit-= 1
            print("guess higher")
            print(f'WRONG GUESS, you are losing one more live {guess_limit}')
            if guess_limit == 0:
                print('You have no lives left: "Lost" GAME OVER')
                return
                
        elif guess > number:
            print("guess lower")    
        else:
            print('you won')       
play_game()
