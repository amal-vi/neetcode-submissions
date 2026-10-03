class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(numbers)):
            diff = target - numbers[i]
            for j in range(len(numbers)):
                if diff == numbers[j]:
                    arr.append(i+1)
                    arr.append(j+1)
                    return arr                    
            
            
