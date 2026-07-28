class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stacktop, stackind=stack.pop()
                result[stackind]=i-stackind
            stack.append((t,i))
        return result
                