class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak =0
            curr = num
            print(curr)
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res