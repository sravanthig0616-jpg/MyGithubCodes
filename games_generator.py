import os

GAMES = [
    "snake","guess-the-number","tic-tac-toe","hangman","rock-paper-scissors","pong",
    "brick-breaker","memory-cards","minesweeper","text-adventure","blackjack","roulette",
    "slot-machine","rpg-battle","simon-says","typing-speed","maze-gen-solver","flappy-bird",
    "platformer-demo","asteroid-shooter","connect-four","checkers","sudoku","2048",
    "pong-ai","battleship","calendar-puzzle","word-search","anagram-game","15-puzzle",
    "rhythm-tap","picture-quiz","reaction-tester","lights-toggle","maze-runner","game-of-life",
    "tower-defense","idle-clicker","dice-mini","treasure-treasure","poker-sim","zero-sum-board",
    "wordle-clone","crossword-mini","color-match","sliding-tiles","incremental-sim",
    "tactics-demo","quiz-game","chat-guess"
]

README = "# {name}\n\nA small game named {name}.\nRun using: python main.py\n"

MAIN_CODE = """print("Starter for {name}")"""

for game in GAMES:
    os.makedirs(game, exist_ok=True)

    with open(f"{game}/README.md", "w") as f:
        f.write(README.format(name=game))

    with open(f"{game}/main.py", "w") as f:
        f.write(MAIN_CODE.format(name=game))

print("✔ 50 game folders created successfully!")
