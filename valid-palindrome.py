# 125
# https://leetcode.com/problems/valid-palindrome/

import re


def isPalindrome(s: str) -> bool:
    s = re.sub("[_\W]", "", s).lower()
    return s == s[::-1]