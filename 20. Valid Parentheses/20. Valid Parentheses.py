class Solution:
    def isValid(self, s: str) -> bool:
        slovar = {')': '(', ']': '[', '}': '{'}
        spisok = []
        for char in s:
            if char in slovar:
                if not (spisok and (spisok.pop()==slovar[char])):
                    return False
            else:
                spisok.append(char)

        return not spisok