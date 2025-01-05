class Solution:
    def firstUniqChar(self, s):
        # Create a dictionary to store the frequency of each character
        char_count = {}

        # Count the frequency of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Find the first character with a frequency of 1
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index

        # If no unique character is found, return -1
        return -1

# Instantiation of the Solution class
solution = Solution()

# Testing the functions 
s1 = "leetcode"
s2 = "loveleetcode"
print(solution.firstUniqChar(s1))  
print(solution.firstUniqChar(s2))  #Output 2

