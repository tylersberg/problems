# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
#     For example, 121 is a palindrome while 123 is not.

# Solution using strings is very simple
def isPalinStr(x: int) -> bool:
    return str(x) == str(x)[::-1]


# Solution without converting to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        # Negative numbers and numbers ending in zero are not palindromes
        if x < 0 or x % 10 == 0:
            return False
        # Extract digits from number until we have at least half.
        reversed = 0
        while reversed < x:
            reversed = (reversed * 10) + (x % 10)
            x //= 10

        # If x was odd, x should be compared to reversed without last digit.
        return (x == reversed or x == reversed // 10)


if __name__ == '__main__':
    # Put tests here
    print(Solution().isPalindrome(121))
