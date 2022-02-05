import math

class Solution:
    def maximum(self, A, l, r):
        if r - l == 0:
            return A[r]
        
        lmax = self.maximum(A, l, int(math.floor((l + r) / 2)))
        rmax = self.maximum(A, int(math.floor((l+r) / 2) + 1), r)
        print(rmax, lmax)
        if rmax < lmax:
            return lmax
        return rmax
    
A = [0, 10, 8, 6, 4, 2]
run = Solution()
run.maximum(A, 1, 5)


class SolutionII:
    def MaxMin(i, j, max, min):
        if i == j:
            max = min = a[i]
        elif i == j-1:
            if a[i] < a[j]:
                max = a[j]
                min = a[i]
            else:
                max = a[i]
                min = a[j]
        else:
            mid = ( i + j )/2
            MaxMin( i, mid, max, min )
            MaxMin( mid+1, j, max1, min1 )
            
            if max < max1:
                max = max1
            if min > min1:
                min = min1

class HanoiTower:
    def output(self, origin, destination):
        print("Move the top disk " + str(origin) + " to rod " + str(destination))
    
    def move(self, n, start, end):
        if start != 1 and end != 1:
            temp = 1
        elif start != 2 and end != 2:
            temp = 2
        else:
            temp = 3

        if n == 1:
            self.output(start, end)
        else:
            self.move(n-1, start, temp)
            self.move(1, start, end)
            self.move(n-1, temp, end)
    
obj = HanoiTower()
obj.move(3, 1, 3)