# ----------------- Arrays & Hashing -----------------
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # {1:3, 2:2, 3:1}
        freq = [[] for i in range(len(nums) + 1)]  # [[], [], [], []]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, value in count.items():
            freq[value].append(key)

        # print(freq) #  [[], [3], [2], [1], [], [], []]
        res = []
        for i in range(
            len(freq) - 1, 0, -1
        ):  # # loop through freq in reverse, then store values in res, once k equals res return result.
            for n in freq[i]:
                res.append(n)
                if k == len(res):
                    return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


"""
128. Longest Consecutive Sequence
return the length of the longest conseccutive elments sequence.
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if start of sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


# ----------------- Two Pointers -----------------
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Approach:
1. sort the nums
2. iterate nums, edge cases greater than zero skip and index greater than zero and current and previous arent the same 
3. do regular two pointer
4. shrink window otherwise add the triplets
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all triplets that equals to zero, must not contain duplicate triplets
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # skip positive integers
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:  # shrink right side
                    r -= 1
                elif threeSum < 0:  # shrink left side
                    l += 1
                else:  # return result
                    res.append([a, nums[l], nums[r]])
                    l += 1  # shrink window
                    r -= 1
                    while (
                        nums[l] == nums[l - 1] and l < r
                    ):  # move left pointer when l and prev are the same and ensure it doesn't go out of bounds
                        l += 1
        return res


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # return the maximum amount of water a container can store
        # [1,8,6,2,5,4,8,3,7] , 7 * 7 = 49
        # if left is less than right the water will overflow
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            area = min(height[r], height[l]) * (r - l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return res


# ----------------- Sliding Window -----------------
"""
Input: prices = [7,1,5,3,6,4]
profit = buy low on day one sell high future day
buy = 1, sell =6 , profit = 5

Output: 5
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return the maximum profit you can achieve
        res = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


"""
 find the length of the longest substring without repeating characters.
 sliding window + hashset
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, r - l + 1)
        return res


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # change character to uppercase k times, i wanna know the longest substring containing same letter
        # "ABAB", k=2 , output=4 , we change A or B k times(2) we get 4 substring

        # sliding window +  char count
        l, maxf = 0, 0
        count = {}

        for r in range(len(s)):
            # expand window + calc maxf
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # shrink window
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
        return r - l + 1  # how did i get access to r from here??


"""
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# sliding window + hashset
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        # store t count in hashset
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            # expand window
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            # shrink window
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


# ----------------- Stack -----------------


# store pair in hashKey, use stack to check if matches hashKey
# Stack follows LIFO while Queue follows FIFO data structure type.
class Solution:
    def isValid(self, s: str) -> bool:
        # [( )]
        hashKey = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c not in hashKey:
                stack.append(c)
                continue
            if not stack or hashKey[c] != stack[-1]:
                return False
            stack.pop()
        return not stack


# ----------------- Binary Search -----------------
"""
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        curr_min = float("inf")

        while start < end:
            mid = start + (end - start) // 2  # pivot
            curr_min = min(curr_min, nums[mid])  # store current min

            # decide where to place indices
            # right has the min
            if nums[mid] > nums[end]:
                start = mid + 1
            # left has the min
            else:
                end = mid - 1
        return min(curr_min, nums[start])


"""
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

"""


# check wether to do binary search on left sorted or right sorted move pointer based on pivot middle less than or greater than
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # left sorted position
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted position
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# ----------------- Linked List -----------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next  # store original curr
            curr.next = prev  # set curr next to prev
            prev = curr  # prev to next swap
            curr = temp  # grab original temp set to curr
        return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow.val , fast.val) # slow == 2, fast ==4

        # reverse second half
        second = slow.next
        prev = slow.next = None
        # print(second.val, prev) # 3 None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # print(prev.val) # 4

        # merge two halfs
        first, second = head, prev  # 1, 4
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


# ----------------- Trees -----------------
# ----------------- Tries -----------------
# ----------------- Heap/Priority Queue -----------------
# ----------------- Backtracking -----------------
# ----------------- Graphs -----------------
# ----------------- Advanced Graphs -----------------
# ----------------- 1-D Dynamic Programming -----------------
# ----------------- 2-D Dynamic Programming -----------------
# ----------------- Greedy -----------------
# ----------------- Intervals -----------------
# ----------------- Math & Geometry -----------------
# ----------------- Bit Manipulation -----------------
