import re

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        split_s = re.split(r"([+\-*/])", s)
        stack = []
        i = 0

        while i < len(split_s):
            item = split_s[i]
            match(item):
                case '*':
                    multi_val = stack.pop()
                    stack.append(multi_val * int(split_s[i+1]))
                case '/':
                    divid_val = stack.pop()
                    stack.append(int(divid_val / int(split_s[i+1])))
                case '-':
                    stack.append(int(item + split_s[i+1]))
                case '+':
                    i += 1
                    continue
                case _:
                    stack.append(int(item))
                    i += 1
                    continue
            i += 2
        return sum(stack)