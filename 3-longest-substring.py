class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        begin = 0
        end = 0

        hash_s = {}

        for char in s:
            if (char in hash_s) and (hash_s[char] >= begin):
                begin = hash_s[char] + 1
            hash_s[char] = end
            end += 1
            length = max(length, end-begin)

        return length