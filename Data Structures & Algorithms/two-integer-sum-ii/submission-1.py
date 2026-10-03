class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # arr = []
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     for j in range(len(numbers)):
        #         if diff == numbers[j]:
        #             arr.append(i+1)
        #             arr.append(j+1)
        #             return arr      
        h , t = 0 , len(numbers)-1

        while h < t:
            curSum = numbers[h] + numbers[t]
            if curSum > target:
                t-=1
            elif curSum < target:
                h+=1
            else:
                return [h+1,t+1]
        return []                              
            
            
