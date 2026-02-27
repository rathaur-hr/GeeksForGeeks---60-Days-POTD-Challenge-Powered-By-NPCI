class Solution:
    def areIsomorphic(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        m1, m2 = {}, {}
        for a, b in zip(s1, s2):
            if (a in m1 and m1[a] != b) or (b in m2 and m2[b] != a):
                return False
            m1[a] = b
            m2[b] = a
        return True