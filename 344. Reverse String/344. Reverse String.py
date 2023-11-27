class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            tmp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = tmp