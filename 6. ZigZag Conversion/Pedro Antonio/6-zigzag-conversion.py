#Tempo: O(n)
#Espaço: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s;

        answer = ""
        s_len = len(s)
        cycleLen = 2 * numRows - 2

        for i in range(numRows):
            j = 0
            while j + i < s_len:
                answer += s[j+i]
                if (i != 0) and (i != numRows -1) and (j + cycleLen - i < s_len):
                    answer += s[j + cycleLen - i]
                j+=cycleLen

        return answer