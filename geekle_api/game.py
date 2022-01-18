from datetime import datetime
from enum import IntEnum
import time
from geekle_api.reader import Reader


class Match(IntEnum):
    WRONG_LETTER = 0
    CORRECT_LETTER_BUT_WRONG_SPOT = 1
    CORRECT_LETTER_AND_SPOT = 2


class Game(object):
    def __init__(self, reader: Reader) -> None:
        self.reader = reader
        self.start()

    def start(self) -> None:
        unixtime = self._current_date_to_unix_time()
        self._word_of_the_day = self.reader.read_index(unixtime).upper()

    def guess_word(self, guess: str) -> list[Match]:
        guess = guess.upper()
        if len(guess) != len(self._word_of_the_day):
            raise ValueError(
                f"Guess must be {len(self._word_of_the_day)} characters long"
            )

        matches = []
        for i, char in enumerate(guess):
            if char == self._word_of_the_day[i]:
                matches.append(Match.CORRECT_LETTER_AND_SPOT)
            else:
                if char in self._word_of_the_day:
                    matches.append(Match.CORRECT_LETTER_BUT_WRONG_SPOT)
                else:
                    matches.append(Match.WRONG_LETTER)

        return matches

    def get_word_of_the_day(self) -> str:
        return self._word_of_the_day

    def _current_date_to_unix_time(self) -> int:
        today = datetime.today()
        date_string = f"{today.day}/{today.month}/{today.year}"
        date = datetime.strptime(date_string, "%d/%m/%Y")
        return int(time.mktime(date.timetuple()))
