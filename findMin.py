# 运用二分法，左右两个指针同中间值比较，直至找到最小值
# 时间复杂度O(logn)

class Solution:
	def findMin(self, nums):
		if nums[0] < nums[len(nums) - 1]:
			return nums[0]
		else:
			l = 0; r = len(nums) - 1
			while l < r and nums[l] > nums[r]:
				m = (l + r) // 2
				if nums[m] < nums[r]:
					r = m
				else:
					l += 1
			return nums[l]

a = [3,4,5,1,2]
fin = Solution()
print(fin.findMin(a))