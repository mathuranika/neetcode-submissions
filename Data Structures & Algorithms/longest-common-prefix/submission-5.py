class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs);
        n = len(sorted_strs)

        first = sorted_strs[0]
        last = sorted_strs[n-1]

        res = "";

        for i in range(0,len(first)):
            if first[i] == last[i]:
                res += first[i]
            else:
                break

        return res
