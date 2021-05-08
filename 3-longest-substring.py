class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        begin = 0
        end = 0

        hash_s = {}

        for i in range(len(s)):
            if (hash_s.get(s[i]) != None) and (hash_s.get(s[i]) >= begin):
                begin = hash_s.get(s[i]) + 1
            hash_s[s[i]] = end
            end += 1
            length = max(length, end-begin)
        

        return length