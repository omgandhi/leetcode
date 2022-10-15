# 21
# https://leetcode.com/problems/valid-parentheses/

class ValidParentheses:
    def checker(self, char):
        openingRound = "("
        openingSquare = "["
        closingRound = ")"
        closingSquare = "]"
        closingCurly = "}"
        if char == openingRound:
            return closingRound
        elif char == openingSquare:
            return closingSquare
        else:
            return closingCurly

    def isValid(self, s: str) -> bool:
        closing = [")", "]", "}"]
        expected = []
        for char in s:
            if expected is []:
                expected.append(self.checker(char))
            elif expected == char:
                expected.pop(0)
            elif char in closing:
                return False
            else:
                expected.insert(0, char)
        return True

    def submission(self, s: str) -> bool:
        openingRound = "("
        openingSquare = "["
        closingRound = ")"
        closingSquare = "]"
        closingCurly = "}"
        closing = [")", "]", "}"]
        expected = []
        for char in s:
            if not expected:
                if char == openingRound:
                    expected.append(closingRound)
                elif char == openingSquare:
                    expected.append(closingSquare)
                else:
                    expected.append(closingCurly)
            elif expected[0] == char:
                expected.pop(0)
            elif char in closing:
                return False
            else:
                if char == openingRound:
                    expected.insert(0, closingRound)
                elif char == openingSquare:
                    expected.insert(0, closingSquare)
                else:
                    expected.insert(0, closingCurly)
        return len(expected) == 0


valid = ValidParentheses()
print(valid.submission("([)]"))
