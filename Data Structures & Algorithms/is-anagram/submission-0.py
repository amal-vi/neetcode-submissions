class Solution:
    def isAnagram(self, s: str, t: str) :
        newS = list(s)
        newS = sorted(newS)
        newT = list(t)
        newT = sorted(newT)
        if newS == newT:
            return True
        return False    

        