# 先将整个字符串反转，再用split()函数按' '拆分单词
# 再将单词以字符串逆序输出

class Solution:
	def reverseWords(self, s: str) -> str:
		rs = []
		for w in s[::-1].split(' '):
			rs.append(w[::-1])
		return ' '.join(rs)

s1 = "the sky is blue"
st = Solution()
print(st.reverseWords(s1))
