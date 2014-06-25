class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        operators = ['+', '-', '*', '/']
        stack = []
        for x in tokens:
            if x in operators:
                b = float(stack.pop())
                a = float(stack.pop())
                # if x == '+':
                #     result = a+b
                # elif x == '-':
                #     result = a-b
                # elif x == '*':
                #     result = a*b
                # elif x == '/':
                #     result = a/b
                result = eval( "%f %s %f"%(a,x,b) )
                stack.append(int(result))
            else:
                stack.append(int(x))
            print x
            print stack
        return stack.pop()

s = Solution()
s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])