# 34. 在排序数组中查找元素的第一个和最后一个位置
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            L = len(nums)-1
            start = nums.index(target)
            nums.sort(reverse=True)
            ending = L - nums.index(target)
            return start, ending
        else:
            return [-1, -1]


Soga = Solution()
nums = [5, 7, 7, 8, 8, 8, 10, 11, 15]
target = 8
Answer = Soga.searchInsert(nums, target)
print(Answer)

# 这题底层一点的代码，需要再搞

# 34. 在排序数组中查找元素的第一个和最后一个位置
# 二分法


class Solution:
    def searchRange(self, nums, target):
        def getRightBorder(nums, target):
            left, right = 0, len(nums) - 1
            rightBoder = -2  # 记录一下rightBorder没有被赋值的情况
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                else:  # 寻找右边界，nums[middle] == target的时候更新left
                    left = middle + 1
                    rightBoder = left

            return rightBoder

        def getLeftBorder(nums, target):
            left, right = 0, len(nums) - 1
            leftBoder = -2  # 记录一下leftBorder没有被赋值的情况
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] >= target:  # 寻找左边界，nums[middle] == target的时候更新right
                    right = middle - 1
                    leftBoder = right
                else:
                    left = middle + 1
            return leftBoder

        leftBoder = getLeftBorder(nums, target)
        rightBoder = getRightBorder(nums, target)
        # 情况一
        if leftBoder == -2 or rightBoder == -2: return [-1, -1]
        # 情况三
        if rightBoder - leftBoder > 1: return [leftBoder + 1, rightBoder - 1]
        # 情况二
        return [-1, -1]


Soga = Solution()
nums = [5, 7, 7, 8, 8, 8, 10, 11, 15]
target = 8
Answer = Soga.searchRange(nums, target)
print(Answer)
