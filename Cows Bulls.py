import random

nums = '0123456789'

def generateSecretNumber():
    """Generates random secret number"""
    secret_number = ''

    while len(secret_number) != 4:
        random_digit = random.choice(nums)
        if random_digit not in secret_number:
            secret_number += random_digit
    return secret_number
 

def checkCowsBulls(secret_number, guessed_number, life):
    """
    Checks bulls and cows returns true if number is cracked else false
    """
    no_of_cows = 0
    no_of_bulls = 0
    if secret_number == guessed_number:
        return True
    else:
        for i in range(4):
            # checks valid digit or not
            if guessed_number[i] in secret_number:
                if guessed_number[i] == secret_number[i]:
                    # correct digit on the correct place
                    no_of_bulls += 1
                else:
                    # correct digits on the wrong place
                    no_of_cows += 1

        print(f"{no_of_bulls} Bulls and {no_of_cows} Cows        [Life : {life}]")
        # print(secret_number)
        return False


if __name__ == "__main__":
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")
    player_attempts = []

    for i in range(1, 3):
        life = 5
        attempts = 0
        secret_number =  generateSecretNumber()
        print("\n" + eval(f"player{i}").title() + "'s turn:")
        guessed_number = input("Guess Number: ")

        while life != 0:
            life -= 1
            attempts += 1
            if len(guessed_number) == 4:
                won = checkCowsBulls(secret_number, guessed_number, life)

                if won:
                    player = eval(f"player{i}").title()
                    print(f"{player} cracked secret number in {attempts} attempt(s)")
                    player_attempts.append(attempts)
                    break
                elif life == 0 and not won:
                    print("\nBetter luck next time!")
                    print(f"Secret number: {secret_number}")
                else:
                    guessed_number = input("\nGuess Number: ")    
            else:
                print("4 Digits required.")
                guessed_number = input("\nGuess Number: ")
        
    if player_attempts == []:
        print("Both failed")
    else:
        player1_attempts, player2_attempts = player_attempts
        if player1_attempts == player2_attempts:
            print("\nTied!")
        elif player1_attempts > player2_attempts:
            print(f"\n{player2.title()} won!")
        else:
            print(f"\n{player1.title()} won!")
        
        

