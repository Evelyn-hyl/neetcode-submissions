class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            temp = (temperatures[i], i)

            while stack and temp[0] > stack[-1][0]:
                popped = stack.pop()
                res[popped[1]] = i - popped[1]
            
            stack.append(temp)
        
        return res
        

