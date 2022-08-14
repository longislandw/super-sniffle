# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    # O(n^2)
    def lengthOfLongestSubstring_init(self, s):
        max = 0
        counter = 0
        start = 0
        for cur in range(len(s)):
            counter += 1
            for check in range(start+1, cur):
                if (s[check] == s[cur]):
                    start = cur
                    if (counter > max):
                        max = counter
                    counter = 0
        return max

    # Hash set O(1)
    def lengthOfLongestSubstring(self, s):
        char_hash = [0]*128
        max = 0
        counter = 0
        start = 0
        for cur in range(len(s)):
            counter += 1
            char = s[cur]
            char_hash[ord(char)] += 1

            while (char_hash[ord(char)] > 1):
                char_hash[ord(s[start])] -= 1
                start += 1
                counter -= 1

            if (counter > max):
                max = counter
        return max


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
