class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t in '+-*/':
                if t=='+':
                    num1=stack.pop()
                    num2=stack.pop()
                    addsum=num2+num1
                    stack.append(addsum)
                if t=='-':
                    num1=stack.pop()
                    num2=stack.pop()
                    sub=num2-num1
                    stack.append(sub)
                if t=='*':
                    num1=stack.pop()
                    num2=stack.pop()
                    mul=num2*num1
                    stack.append(mul)
                if t=='/':
                    num1=stack.pop()
                    num2=stack.pop()
                    div=int(float(num2)/num1)
                    stack.append(div)
            else:
                stack.append(int(t))
        return int(stack[-1])