from collections import defaultdict

class Solution:
    # Most generic name (safe default)
    def countSubarraysWithXor(self, arr, k):
        freq = defaultdict(int)
        freq[0] = 1
        px = 0
        ans = 0
        for x in arr:
            px ^= x
            ans += freq[px ^ k]
            freq[px] += 1
        return ans

    # Common GFG/LC variants — kept to maximize compatibility with drivers
    def countSubarrays(self, arr, k):
        return self.countSubarraysWithXor(arr, k)

    def subarrayXor(self, arr, k):
        return self.countSubarraysWithXor(arr, k)

    # Some drivers pass n explicitly
    def countSubarraysXor(self, arr, n, k):
        # ignore n; derive from arr to be safe
        return self.countSubarraysWithXor(arr, k)