class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        for s in strs:
            count = [0] * 26 #set a-z to 0 for all the words 

            for c in s: 
                count[ord(c)-ord("a")] += 1 #increment count of char by 1 
                # print(count)

            res[tuple(count)].append(s) 

        return list(res.values())

        
