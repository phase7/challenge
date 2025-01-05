
from functools import cache
import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        s = list(s)
        rep = np.zeros(len(s), dtype=int)

        @cache
        def shifted_char(c: str, shift: int = 1) -> str:
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))


        for start, end, direction in shifts:
            shift = 1 if direction else -1
            rep[start:end+1] += shift

        return "".join([shifted_char(c, shift) for c, shift in zip(s, rep)])

if __name__ == "__main__":
    assert Solution().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]) == "ace", Solution().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])
    assert Solution().shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]]) == "catz", Solution().shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]])