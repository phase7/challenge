class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        # each idx is dist to other 1s
        # can count balls on left side, calls on right side
        # and kind of slide a pivot

        # we might need 2 passes?

        # print('ones: ', one_count)
        left_ones = 0
        res = [0]*len(boxes)
        dist = 0
        for i,c in enumerate(boxes):
            # for each 1 you have seen on the left, its distance grows by one
            dist += left_ones
            res[i] = dist 

            if c == '1':
                left_ones += 1

        right_ones = 0
        dist = 0
        for i in range(len(boxes) -1, -1, -1):
            c = boxes[i]

            dist += right_ones
            res[i] += dist
            if c == '1':
                right_ones += 1
        return res
    
if __name__ == "__main__":
    assert Solution().minOperations(boxes = "110") == [1,1,3], Solution().minOperations(boxes = "110")
    assert Solution().minOperations(boxes = "001011") == [11,8,5,4,3,4], Solution().minOperations(boxes = "001011")