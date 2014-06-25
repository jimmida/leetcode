# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        l = len(points)
        if l == 1:
            return 1
        lines = {}
        for i in range(l):
            for j in range(i+1,l):
                p1 = points[i]
                p2 = points[j]
                key1 = "%i:%i" % (p1.x, p1.y)
                key2 = "%i:%i" % (p2.x, p2.y)
                if key1 == key2:
                    continue
                line = self.find_line(p1, p2)
                if line not in lines:
                    lines[line] = {}
                lines[line][p1] = 0
                lines[line][p2] = 0
        print lines
        pts = [len(lines[line].values()) for line in lines]
        return max(pts)
    
    def find_line(self, p1, p2):
        if p2.x-p1.x == 0:
          return 'x%i:x'
        slope = (p2.y-p1.y)/float(p2.x-p1.x)
        intcp = p1.y-slope*p1.x
        return "%f:%f" % (intcp, slope)
