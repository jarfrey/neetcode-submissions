class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(t)
        t1 = sorted(s)
        if s1 == t1:
            return True
        return False