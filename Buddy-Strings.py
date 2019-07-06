class Solution:
	def buddyStrings(self, A: str, B: str) -> bool:
		#	首先需要判断 两个字符串的长度是否相等，
		#	如果不相等，怎么交换都无法使得两个字符串相等，返回False
		if len(A) != len(B):
			return False

		#	若字符串A和B相等，A或B中有重复的字符，则为亲密字符串，返回True
		#	反之，返回False
		elif A == B:
			bset = set()
			for i in B:
				if i in bset:
					return True
				bset.append(i)
			return False

		#	若字符串A和B不相等，存在A[i] == B[j],A[j] == B[i],且A和B除
		#	A[i]-B[i]、A[j]-B[j]外，对应元素都相等
		else:
			l = []
			A, B = list(A), list(B)
			C = zip(A,B)
			print(C)
			for i, j in C:
				if i != j:
					l.append([i,j])
			return len(l) == 2 and l[0] == l[1][::-1]

s1, s2 = "aaaaaaabc", "aaaaaaacb"
string1 = Solution()
b = string1.buddyStrings(s1,s2)
print(b)

