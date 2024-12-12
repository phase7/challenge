from heapq import heapify, heappop, heappush
from math import sqrt, floor

bridge_sqrt = lambda x: -1 * floor(sqrt(-x))

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [x*-1 for x in gifts]
        heapify(gifts)
        for _ in range(k):
            get_pile = bridge_sqrt(heappop(gifts))
            heappush(gifts, get_pile)
        return -1 * sum(gifts)

if __name__ == "__main__":
    assert Solution().pickGifts(gifts = [25,64,9,4,100], k = 4) == 29
    assert Solution().pickGifts(gifts = [1,1,1,1], k = 4) == 4