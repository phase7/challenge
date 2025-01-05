
from string import ascii_lowercase
from functools import cache
from typing import Literal

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        @cache
        def shifted_char(c: str, direction : Literal[0,1]) -> str:
            shift = 1 if direction else -1
            if c == 'z' and shift == 1:
                return 'a'
            elif c == 'a' and shift == -1:
                return 'z'
            return ascii_lowercase[ascii_lowercase.index(c) + shift]

        @cache
        def shifted_string(s: str, direction: Literal[0,1]) -> str:
            return ''.join([shifted_char(c, direction) for c in s])
    

        for start, end, direction in shifts:
            chunk = s[start:end+1]
            s.replace(chunk, shifted_string(chunk, direction))
        return s

if __name__ == "__main__":
    assert Solution().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]) == "ace", Solution().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])
    assert Solution().shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]]) == "catz", Solution().shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]])