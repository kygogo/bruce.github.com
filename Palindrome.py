# 回文字符串关于字符中心对称，i:首字符，j:尾字符
# i<j 或 j>i 时，跳过非数字或字符的元素，循环中若
# 出现不匹配的元素则返回False
class Solution:
	def isPalindrome(self, s: str) -> bool:
		i, j = 0, (len(s)-1)
		while i < j:
			while i < j and not s[i].isalnum():
				i += 1
			while i < j and not s[j].isalnum():
				j -= 1
			if s[i].lower() != s[j].lower():
				return False
			i += 1 
			j -= 1
		return True

s = "A man, a plan, a canal: Panama"
string1 = Solution()
b = string1.isPalindrome(s)
print(b)