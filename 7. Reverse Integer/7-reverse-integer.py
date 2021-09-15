#Tempo: O(n) *Não tenho certeza
#Memoria: O(n)
MIN_INT = -2147483648
MAX_INT = 2147483647

class Solution:
    def reverse(self, x: int) -> int:
        signed = str(x)[0] == '-'
        str_x = str(x)[signed:]
        reversed_x = int('-'*signed + str_x[::-1])

        return reversed_x if (reversed_x >= MIN_INT) and (reversed_x <= MAX_INT) else 0