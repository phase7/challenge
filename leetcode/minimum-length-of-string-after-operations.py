
from string import ascii_lowercase
class Solution:
    def minimumLength(self, s: str) -> int:
        ans = len(s)
        for char in set(ascii_lowercase):
            v = s.count(char)
            if v > 2:
                # time to operate
                ans -= (v - 1)
                if not(v & 1):
                    ans += 1

        return ans


if __name__ == "__main__":
    s = Solution()

    assert s.minimumLength("ca") == 2, s.minimumLength("ca")
    assert s.minimumLength("abaacbcbb") == 5, s.minimumLength("abaacbcbb")