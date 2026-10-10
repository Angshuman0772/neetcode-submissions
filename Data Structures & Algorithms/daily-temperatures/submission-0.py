class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # while stack is not empty and the current temp is greater than last stack temperature
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (i - stackInd)
            stack.append([t, i])
        return result
