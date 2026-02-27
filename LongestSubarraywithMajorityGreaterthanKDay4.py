class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        pref = [0] * (n + 1)
        for i, x in enumerate(arr, 1):
            pref[i] = pref[i - 1] + (1 if x > k else -1)

        st = []
        for i in range(n + 1):
            if not st or pref[i] < pref[st[-1]]:
                st.append(i)

        ans = 0
        for j in range(n, -1, -1):
            while st and pref[j] > pref[st[-1]]:
                ans = max(ans, j - st[-1])
                st.pop()
        return ans