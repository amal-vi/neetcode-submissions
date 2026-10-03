class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        #brute force method
        # for n in range(len(nums)):
        #     for j in range(n+1,len(nums)):
        #         if nums[n]==nums[j]:
        #             return True
        # return False    

        #optimized code using hashmap

        hashSet = set()

        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False        

