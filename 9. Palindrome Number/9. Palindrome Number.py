class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = str(x)
        return ''.join(reversed(self.x))==self.x
