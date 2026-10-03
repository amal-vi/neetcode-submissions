class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashSet = {}
        freq = [[] for i in range(len(nums) + 1 )]

        for n in nums:
            hashSet[n] = 1 + hashSet.get(n,0)

        for num,cnt in hashSet.items():
            freq[cnt].append(num)
        print(freq)    

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    

            