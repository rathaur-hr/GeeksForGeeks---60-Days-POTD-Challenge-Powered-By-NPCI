class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        write = 0
        for read in range(n):
            if arr[read] != 0:
                if write != read:
                    arr[write] = arr[read]
                write += 1
        while write < n:
            arr[write] = 0
            write += 1