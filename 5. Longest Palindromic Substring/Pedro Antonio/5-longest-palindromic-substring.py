class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = s.replace('','#')
        p = [0]*len(s)
        center = 0
        boundary = 0
        i = 0
        longest_idx = 0
            
        while boundary < len(s) and i < len(s):
            mirror = center - (i - center)

            p[i] = min(p[mirror], boundary-i) if i < boundary else p[i]
            
            left = i - p[i] - 1
            right = i + p[i] + 1

            while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
                p[i] += 1
                right += 1
                left -= 1

            if (i + p[i] > boundary):
                center = i
                boundary = i + p[i]
            longest_idx = i if p[longest_idx] < p[i] else longest_idx

            i += 1
        return s[longest_idx - p[longest_idx] : longest_idx + p[longest_idx]].replace('#','')