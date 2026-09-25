class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_len = len(temperatures)
        currIndex = 0
        result = [0] * temp_len
        stack = []
        

        for currIndex in range(temp_len):
            while stack and temperatures[currIndex] > stack[-1][0]:
                temp, ind = stack.pop()
                result[ind] = currIndex - ind
            stack.append((temperatures[currIndex], currIndex))
            currIndex += 1
        
        return result

