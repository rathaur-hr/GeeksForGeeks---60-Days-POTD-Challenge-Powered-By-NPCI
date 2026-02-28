class Solution:
    def findClosestPair(self, arr1, arr2, x):
        n, m = len(arr1), len(arr2)
        i, j = 0, m - 1
        best_diff = float('inf')
        best_pair = [arr1[0], arr2[0]] 
        while i < n and j >= 0:
            s = arr1[i] + arr2[j]
            diff = abs(s - x)

            if diff < best_diff:
                best_diff = diff
                best_pair = [arr1[i], arr2[j]]

            if s > x:
                j -= 1
            elif s < x:
                i += 1
            else:
                return [arr1[i], arr2[j]]

        return best_pair
    def printClosest(self, arr1, arr2, x):
        return self.findClosestPair(arr1, arr2, x)
