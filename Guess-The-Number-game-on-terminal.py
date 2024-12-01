import random
import webbrowser
import time
import subprocess
import sys

#Ensure pyautogui is installed, if not asks the user if they want to install pyautogui
try:
    import pyautogui
except ImportError:
    install_choice = input("The 'pyautogui' module is required for this game. Would you like to install it? (yes[y]/no[n]): ").strip().lower()
    if install_choice in ("yes", "y"):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
            import pyautogui
        except Exception as e:
            print(f"Failed to install 'pyautogui'. Please install it manually.\nError: {e}")
            exit()
    else:
        print("Cannot proceed without 'pyautogui'. Exiting the game.")
        exit()

def number_guess():
    print("\n=== Start New Game ===")
    print("I think of number from 1 to 100. Can you guess it? My great Adventurer!")
    
    guess_number = random.randint(1, 100)
    try:
        attempts = int(input("How many attempts would you like?: "))
        
        #messages based on the amount of attempts
        if attempts >= 10000:
            print("\033[1m")  #bold text
            print("MATE MY GRANDMA CAN GUESS IT IN 7 ATTEMPTS! WHAT THE HELL YOU NEED THAT MUCH ATTEMPTS?... WHY...? JUST WHY...?")
            print("\033[0m")
        elif 41 <= attempts <= 9999:
            print("I think that is gonna make it too easy, mate!")
        elif 15 <= attempts <= 40:
            print("U want it easy, huh?")
        elif 7 <= attempts <= 14:
            print("Good choice of balance.")
        elif 5 <= attempts <= 6:
            print("Might be challenging.")
        elif attempts == 4:
            print("You want to challenge yourself, huh?...")
        elif attempts == 3:
            print("It will be hard... I warned ya.")
        elif attempts == 2:
            print("Why you gotta go hard on yourself?")
        elif attempts == 1:
            print("One shot man, huh...?\nI think this is perfect song for you, it's on YouTube!: youtube.com/watch?v=998Kyw2FmU4&t=48s")
            webbrowser.open("https://www.youtube.com/watch?v=998Kyw2FmU4&t=48s")

            time.sleep(0.5)
            
            pyautogui.keyDown("alt")  #holds Alt key
            pyautogui.press("tab")    #presses Tab
            pyautogui.keyUp("alt")    #releases Alt
            print("Switched back to the editor.\n")
            print("\nWait, think carefully before choosing a number, it might help to think.")
            time.sleep(3)

    except ValueError:
        print("Invalid input. Defaulting to 7 attempts.")
        attempts = 7  #if invalud value, defaults back to 7
    
    time.sleep(0.5)
    #game loop
    while attempts > 0:
        try:
            guess = int(input(f"\nYou have {attempts} attempts left. Your guess: "))
            
            if guess < guess_number:
                print("Too low!")
            elif guess > guess_number:
                print("Too high!")
            else:
                print(f"🎉 Congrats! You guessed the number {guess_number} with {attempts - 1} attempts left! You win! 🎉")
                return
            
            attempts -= 1
        except ValueError:
            print("Please enter a valid number.")
    
    #loser message
    print(f"\nWelp... That's it... better luck next time! btw the number was {guess_number}")

def credits():
    print("\n=== About / Credits ===")
    print("This game is made by Ellie in their basement on the hard cold floor. LMAO!")
    print("IG: https://www.instagram.com/evixosity/\n")
    input("Press Enter to return to the main menu.")

def main_menu():
    while True:
        print("\033[95m")  #color to pink
        print("Welcome to Guess the Number mini-game!")
        print("\033[0m")  #color reset
        print("1. Start new game!")
        print("2. About / Credits")
        print("0. Exit the game")

        choice = input("Choose an option: ")
        
        if choice == "1":
            number_guess()
        elif choice == "2":
            credits()
        elif choice == "0":
            print("Thanks for playing! Good luck on your next journey, Adventurer!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
