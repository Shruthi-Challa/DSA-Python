class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freq={}
        for ch in magazine:
            freq[ch]=freq.get(ch,0)+1
        for ch in ransomNote:
            if ch not in freq or freq[ch]==0:
                return False
            freq[ch]-=1
        return True