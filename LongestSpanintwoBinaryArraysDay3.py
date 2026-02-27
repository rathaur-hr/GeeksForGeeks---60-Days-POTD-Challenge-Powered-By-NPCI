class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
        prefix_sum = 0
        first_occ = {}
        max_len = 0
        
        for i in range(n):
            prefix_sum += a1[i] - a2[i]
            if prefix_sum == 0:
                max_len = i + 1
            if prefix_sum in first_occ:
                max_len = max(max_len, i - first_occ[prefix_sum])
            else:
                first_occ[prefix_sum] = i
        return max_len