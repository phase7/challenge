class Solution:
    def maxScore(self, binstr: str) -> int:
        ans = 0
        zero_count = 0
        ones = int(binstr, 2).bit_count()

        for i in range(len(binstr) - 1):
            if binstr[i] == '0':
                zero_count += 1
            else:
                ones -= 1
            ans = max(ans, zero_count + ones)
        return ans

if __name__ == '__main__':
    assert Solution().maxScore("00111") == 5
    assert Solution().maxScore("011101") == 5, Solution().maxScore("011101")
    assert Solution().maxScore("1111") == 3