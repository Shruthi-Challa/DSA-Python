class Solution(object):
    def isIsomorphic(self, s, t):
        ST={}
        TS={}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 in ST:
                if ST[c1] != c2:
                    return False
            else:
                ST[c1] = c2

            if c2 in TS:
                if TS[c2] != c1:
                    return False
            else:
                TS[c2] = c1
        return True