#Increase the value of how many hours spent trying to do and understand ANSI codes: 4

import random
import webbrowser
import time
import subprocess
import sys

#Ensure pyautogui is installed, if not asks the user if they want to install pyautogui
try:
    import pyautogui
except ImportError:
    install_choice = input("\033[38;2;92;255;168mThe 'pyautogui' module is required for this game. Would you like to install it?\033[0m (yes[y]/no[n]): ").strip().lower()
    if install_choice in ("yes", "y"):
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
            import pyautogui
        except Exception as e:
            print(f"\033[1m\033[38;2;255;90;90m""Failed to install 'pyautogui'. Please install it manually.\nError: {e}""\033[0m")
            exit()
    else:
        print("\033[38;2;255;136;25mCannot proceed without 'pyautogui'. Exiting the game.\033[0m")
        exit()

def number_guess():
    print("\n\033[38;2;208;133;255m=== Start New Game ===\033[0m")
    print("\033[38;2;102;255;140mI think of number from 1 to 100. Can you guess it? My great Adventurer!\033[0m")
    
    guess_number = random.randint(1, 100)
    try:
        attempts = int(input("\033[38;2;112;210;255mHow many attempts would you like?: \033[0m"))
        
        #messages based on the amount of attempts
        if attempts >= 10000:
            print("\033[1m\033[38;2;255;90;90mMATE MY GRANDMA CAN GUESS IT IN 7 ATTEMPTS! WHAT THE HELL YOU NEED THAT MUCH ATTEMPTS?... WHY...? JUST WHY...?")
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
        print("\033[1m\033[38;2;255;90;90mInvalid input.\033[0m Defaulting to 7 attempts.")
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
            print("\033[1m\033[38;2;255;90;90mPlease enter a valid number.\033[0m")
    
    #loser message
    print(f"\nWelp... That's it... better luck next time! btw the number was {guess_number}")

def credits():
    print("\033[48;2;91;206;250m\033[38;2;91;206;250m__\033[0m")
    print("\033[48;2;245;169;184m\033[38;2;245;169;184m__\033[0m")
    print("\033[48;2;255;255;255m\033[38;2;255;255;255m__\033[0m")
    print("\033[48;2;245;169;184m\033[38;2;245;169;184m__\033[0m")
    print("\033[48;2;91;206;250m\033[38;2;91;206;250m__\033[0m")
    print("\n\n\033[1m\033[38;2;0;0;0m\033[48;2;245;169;211m=== About / Credits ===\033[0m\n")
    print("This game is made by Ellie in their basement on the hard cold floor. LMAO!")
    print("IG: https://www.instagram.com/evixosity/\n")
    input("Press Enter to return to the main menu.")

def license():
    print("\033[1m\033[38;2;255;190;0m\033[48;2;145;61;184m\n\n=== License ===\033[0m\n")
    print("MIT License\n")
    print("Copyright (c) 2024 Ellie\n")
    print("Permission is hereby granted, free of charge, to any person obtaining a copy")
    print("of this software and associated documentation files (the 'Software'), to deal")
    print("in the Software without restriction, including without limitation the rights")
    print("to use, copy, modify, merge, publish, distribute, sublicense, and/or sell")
    print("copies of the Software, and to permit persons to whom the Software is")
    print("furnished to do so, subject to the following conditions:\n")
    print("The above copyright notice and this permission notice shall be included in all")
    print("copies or substantial portions of the Software.\n")
    print("THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR")
    print("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,")
    print("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE")
    print("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER")
    print("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,")
    print("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE")
    print("SOFTWARE.")
    input("\nPress Enter to return to the main menu.")

def main_menu():
    while True:
        print("\n\n\033[0m\033[38;2;245;169;215mWelcome to Guess the Number mini-game!\033[0m\n\n")    #color to pink then reset
        print("1. Start new game!")
        print("2. About / Credits")
        print("3. License")
        print("0. Exit the game")

        choice = input("Choose an option: ")
        
        if choice == "1":
            number_guess()
        elif choice == "2":
            credits()
        elif choice == "3":
            license()
        elif choice == "0":
            print("Thanks for playing! Good luck on your next journey, Adventurer!")
            break
        else:
            print("\033[1m\033[38;2;255;90;90mInvalid choice. Please try again.\033[0m")

main_menu()
