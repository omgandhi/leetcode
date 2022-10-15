# 242
# https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str) -> bool:
    for letter in s:
        if letter in t:
            t = t.replace(letter, "", 1)
            s = s.replace(letter, "", 1)
        else:
            return False
    return s == t