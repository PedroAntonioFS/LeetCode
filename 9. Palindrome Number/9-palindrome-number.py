#Tempo O(1)
#Espaço O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]