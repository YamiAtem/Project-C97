import random
import tts


def start(number: int, difficulty: str, guesses: int):
    tts.speak("Welcome to the number guessing game")
    tts.speak("Pick a difficulty between Easy, Normal, and Hard")
    difficulty_prompt: str = input("Difficulty: ")

    if difficulty_prompt.lower() == "easy":
        tts.speak("You picked easy difficulty so you have to guess a number between 1-5 and you have 3 guesses")
        difficulty = "easy"
        number = random.randint(1, 5)
        guesses = 3
    elif difficulty_prompt.lower() == "normal":
        tts.speak("You picked normal difficulty so you have to guess a number between 1-9 and you have 5 guesses")
        difficulty = "normal"
        number = random.randint(1, 9)
        guesses = 5
    elif difficulty_prompt.lower() == "hard":
        tts.speak("You picked hard difficulty so you have to guess a number between 1-15 and you have 7 guesses")
        difficulty = "hard"
        number = random.randint(1, 15)
        guesses = 7

    return number, difficulty, guesses


def run_game(guesses: int, number: int):
    while guesses > 0:
        tts.speak("Guess the Number")

        guess_number_prompt = input("Number: ")
        guessed_number = int(guess_number_prompt)

        if guessed_number > number:
            tts.speak("The number is too high guess a lower number")
            guesses -= 1
            tts.speak("You have " + str(guesses) + " guesses left")
        elif guessed_number < number:
            tts.speak("The number is too low guess a higher number")
            guesses -= 1
            tts.speak("You have " + str(guesses) + " guesses left")
        else:
            tts.speak("HOORAY! YOU GUESSED THE NUMBER, SO YOU WIN")
            break