class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        ...

if __name__ == "__main__":
    assert Solution().minOperations(boxes = "110") == [1,1,3], Solution().minOperations(boxes = "110")
    assert Solution().minOperations(boxes = "001011") == [11,8,5,4,3,4], Solution().minOperations(boxes = "001011")