class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
      m = len(matrix)
      for i in range(m/2):
        for j in range(m-i*2-1):
          jj = j+i
          upper_left  = matrix[i][jj]
          upper_right = matrix[jj][-1-i]
          lower_right = matrix[-1-i][-1-jj]
          lower_left  = matrix[-1-jj][i]

          # print upper_left, upper_right, lower_right, lower_left

          matrix[jj][-1-i] = upper_left
          matrix[-1-i][-1-jj] = upper_right
          matrix[-1-jj][i] = lower_right
          matrix[i][jj] = lower_left

      return matrix

    def print_matrix(self, matrix):
      for line in matrix:
        print line

matrix = [
  [1,  2,  3,  4,  21],
  [5,  6,  7,  8,  22],
  [9,  10, 11, 12, 23],
  [13, 14, 15, 16, 24],
  [25, 26, 27, 28, 29]
]

s = Solution()
s.print_matrix(matrix)
print
matrix_rotated = s.rotate(matrix)
s.print_matrix(matrix_rotated)