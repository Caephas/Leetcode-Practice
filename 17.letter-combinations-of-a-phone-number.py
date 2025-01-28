#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == '':
            print ([])
            return []
        # Mapping of digits to letters
        digitsDict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    
        # Recursive function to generate combinations
        def backtrack(index, path):
            # If the current path is complete, add it to results
            if index == len(digits):
                combinations.append(''.join(path))
                return
            
            # Get letters for the current digit
            possible_letters = digitsDict[digits[index]]
            
            # Iterate through each letter and recurse
            for letter in possible_letters:
                path.append(letter)  # Choose
                backtrack(index + 1, path)  # Recurse
                path.pop()  # Undo choice

        combinations = []
        backtrack(0, [])
        print(combinations)
        return combinations
        
# @lc code=end

Solution().letterCombinations('')