#Tempo O(n)
#Espaço O(n)
MIN_INT = -2147483648
MAX_INT = 2147483647

class Solution:
    def myAtoi(self, s: str) -> int:

        step = 0
        output = ""
        for char in s + '$':
            if step == 0 and char == " ":
                continue
            elif step == 0 and (char == '-' or char == '+'):
                step = 1
                output += char
            elif char.isdigit():
                step = 2
                output += char
            elif step == 2:
                break
            else:
                return 0

        return max(min(int(output), MAX_INT), MIN_INT)