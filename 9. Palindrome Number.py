"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up:
Could you solve it without converting the integer to a string?
"""


class Solution:
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if (x < 0) or (x % 10 == 0 and x != 0):
			return False
		reverted_number = 0
		while x > reverted_number:
			reverted_number = reverted_number * 10 + x % 10
			x = int(x/10)
		return True if x == reverted_number or x == int(reverted_number/10) else False


if __name__ == "__main__":
	s = Solution()
	print(s.isPalindrome(1231))
	print(s.isPalindrome(1221))
	print(s.isPalindrome(-121))
	print(s.isPalindrome(121))
