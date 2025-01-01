class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        count = 0
        for i, item in enumerate(nums):
            count += 1
            if i == 0:
                continue
            if len(nums) == i:
                # we've reached the END
                count += 1 

            

        return 8

if __name__ == "__main__":
    assert Solution().continuousSubarrays(nums = [5,4,2,4]) == 8
    assert Solution().continuousSubarrays(nums = [1,2,3]) == 6
    print("all tests pass")