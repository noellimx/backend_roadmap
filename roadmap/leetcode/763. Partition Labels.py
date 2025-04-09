class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # "ababcc" -> "abab", "cc"

        last = { s[i]: i for i in range(len(s))}
        parts = []


        lbound = 0
        rbound = 0 # right bound
        for i in range(len(s)):
            r = max(last[s[i]], rbound)
            if i == r:
                parts.append(r-lbound+1)
                lbound = r+1
                rbound += 1
            else:
                rbound = r
        return parts