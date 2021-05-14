import guessing_game

number: int = 0
difficulty: str = ""
guesses: int = 0

number, difficulty, guesses = guessing_game.start(number, difficulty, guesses)

guessing_game.run_game(guesses, number)
