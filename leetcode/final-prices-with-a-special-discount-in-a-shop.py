from copy import deepcopy

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer = deepcopy(prices)
        stack = []
        for i in range(len(prices)):
            while stack and (prices[stack[-1]] >= prices[i]):
                answer[stack.pop()] -= prices[i]
            stack.append(i)
        return answer

if __name__ == "__main":
    assert Solution().finalPrices(prices = [1,2,3,4,5]) == [1,2,3,4,5]
    assert Solution().finalPrices(prices = [8,4,6,2,3]) == [4,2,4,2,3]