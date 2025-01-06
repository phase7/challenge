from functools import cache
import numpy
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        rep = numpy.zeros(len(s)+1, dtype=int)

        @cache
        def shifted_char(c: str, shift: int) -> str:
            return chr((ord(c) - 97 + shift) % 26 + 97)


        for start, end, direction in shifts:
            shift = 1 if direction else -1
            rep[start:end+1] += shift

        return "".join(tuple(shifted_char(c, shift) for c, shift in tuple(zip(s, rep))))

if __name__ == "__main__":
    assert Solution().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]) == "ace", Solution().shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]])
    assert Solution().shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]]) == "catz", Solution().shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]])