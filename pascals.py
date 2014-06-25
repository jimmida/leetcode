class Solution:
    # @return a list of integers
    # def getRow(self, rowIndex):
    #   a = rowIndex
    #   result = [0]*(a+1)
    #   for b in range((a+2)/2):
    #     result[b] = self.aCb(a,b)
    #     result[a-b] = result[b]

    #   return result

    # def aCb(self, a, b):
    #   c = a-b
    #   result = 1
    #   for i in range(c):
    #     result = result * (a-i)
    #   for i in range(c):
    #     result = result / (c-i)
    #   return result

    def getRow(self, rowIndex):
      result = [1]*(rowIndex+1)
      for i in range(rowIndex+1):
        for j in range(i-1, 0, -1):
          result[j] = result[j-1] + result[j]
      return result

s = Solution()
# print s.aCb(1,1)
print s.getRow(5)


