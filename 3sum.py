# 可以通过遍历三次列表完成任务，则时间复杂度为O(n^3)
# 为了降低时间复杂度,需要通过排序去重O(logn)，再遍历O(n^2)
# 时间复杂度为O(n^2)。
# 由于列表已经排序，第一次遍历i时，j = 0-i，当遍历第二次时，
# 若元素大于1/2*j，则第二三个元素之和大于j，便可以停止遍历。
# 时间复杂度为O(n^2)
class Solution:
	def threeSum(self, nums):
		if len(nums) < 3:
			return []
		res = []
		nums.sort()    # 排序
		for i in range(len(nums)-2):    # 三数之和，遍历到倒数第二个数停止
			if nums[i] != nums[i - 1] or i == 0:    # 去重
				ts = 0 - nums[i]
				# 当前值下一个是左指针，列表最后一个是右指针
				l, r = i + 1, len(nums) - 1
				# 遍历
				while l < r:
					# 左指针大于ts/2时，或者右指针小于ts/2时，停止遍历
					if nums[l] > ts // 2 or nums[r] < ts // 2:
						break
					rts = nums[l] + nums[r]    # 双指针对应值之和
					if ts == rts:
						res.append([nums[i], nums[l], nums[r]])    # 添加符合值
						# 左指针和右一个相等，或者右指针和左一个相等，则跳过
						while l < r and nums[l] == nums[l + 1]:
							l += 1
						while l < r and nums[r] == nums[r - 1]:
							r -= 1
						l += 1; r -= 1    # 指针移动
					elif rts < ts:
						l += 1
					else:
						r -= 1
		return res

a = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
cal = Solution()
print(cal.threeSum(a))






