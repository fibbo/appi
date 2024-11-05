""" src/wordle.py"""

import random
from typing import final

import requests


@final
class WordleGame:
    """Wordle Game

    Play the famous wordle game in Python"""

    def __init__(self, solution: str) -> None:
        self.solution = solution
        self.guesses = 0
        self.character_frequency: dict[str, int] = {}
        self.wrongly_placed: dict[str, list[int]] = {}
        self.output: list[str] = []
        self.keyboard_layout_us_as_string = """
        Q W E R T Y U I O P
         A S D F G H J K L
           Z X C V B N M
        """

        # We need to update the character map before we start
        self.update_character_map()

    # How often appears each character in the solution
    def update_character_map(self) -> None:
        self.character_frequency = {}
        for char in solution:
            if char in self.character_frequency:
                self.character_frequency[char] += 1
            else:
                self.character_frequency[char] = 1

    # We need to update the frequency map and amend the out put
    # if we previously put a character that is part of the solution in the wrong place
    # but now we found a place where the character is correct.
    def correct_wrongly_placed(
        self,
        current_map: dict[str, int],
        c: str,
    ):
        if current_map[c] == 0 and c in self.wrongly_placed:
            self.output[self.wrongly_placed[c].pop()] = "⬛"
        else:
            current_map[c] -= 1

    # We keep track of all the characters that are in the solution
    # but are in the wrong place so if we find the right place but
    # exhausted the frequency we can amend the output afterwards.
    def add_wrongly_placed(self, index: int, c: str):
        if c in self.wrongly_placed:
            self.wrongly_placed[c].append(index)
        else:
            self.wrongly_placed[c] = [index]

    def play(self) -> None:
        while True:
            print(self.keyboard_layout_us_as_string)
            guess = input()

            if len(guess) != len(solution):
                print("Not the right length")
                continue
            if guess == solution:
                print("🟩 🟩 🟩 🟩 🟩")
                print("You win!")
                break

            current_map: dict[str, int] = self.character_frequency.copy()

            for index, c in enumerate(guess):
                if c == solution[index]:
                    self.output += "🟩"
                    self.correct_wrongly_placed(current_map, c)
                elif c in self.solution and current_map[c] > 0:
                    self.add_wrongly_placed(index, c)
                    self.output += "🟨"
                    current_map[guess[index]] -= 1
                else:
                    if c not in self.character_frequency:
                        self.keyboard_layout_us_as_string = (
                            self.keyboard_layout_us_as_string.replace(c.upper(), "_")
                        )
                    self.output += "⬛"

            print(self.output)
            self.output = []


reponse = requests.get(
    "https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/45c977427419a1e0edee8fd395af1e0a4966273b/wordle-answers-alphabetical.txt"
)

words = reponse.text.split("\n")
solution = random.choice(words)
game = WordleGame(solution)
game.play()
