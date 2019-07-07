# strs如果为空或者长度为0，既len(strs)==0，则返回""
# 通过zip（）函数将不同str的相应字母打包为元组，再
# 转换为集合，有公共前缀则集合长度为1，长度为1的集合
# 的顺序连接即为公共前缀
class Solution:
	def longestCommonPrefix(self, strs: str) -> str:
		lcp = ''
		if len(strs) == 0:
			return ''
		for pack in zip(*strs):
			print(pack)
			if len(set(pack)) == 1:
				lcp += pack[0]
			else:
				return lcp
		return(lcp)

test = ["flower","flow","flight"]
st = Solution()
head = st.longestCommonPrefix(test)
print(head)
