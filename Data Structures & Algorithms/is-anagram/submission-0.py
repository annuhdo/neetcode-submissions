class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 0

            count[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in count:
                return False
            count[t[j]] -= 1

        for letter in count:
            if count[letter] != 0:
                return False

        return True