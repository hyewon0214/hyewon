def heightChecker(heights):
    con=sorted(heights)
    state=0
    for i in range(len(heights)):
        if heights[i]==con[i]:
            state+=1
    return len(heights)-state
#print(heightChecker([1,1,4,2,1,3]))

def intersection(nums1,nums2):
    return list(set(nums1)&set(nums2))
#print(intersection([4,9,5],[9,4,9,8,4]))

def sortedSquares(a):
    for i in range(len(a)):
        a[i] *= a[i]
    a.sort()
    return a
#print(sortedSquares([-4,-1,0,3,10]))

def twoSum(nums,target):
    dic={}
    for i in range(len(nums)):
        value=target-nums[i]
        if value not in dic:
            dic[nums[i]]=i
        elif value in dic:
            return [dic[value], i]
#print(twoSum([3,2,4],6))

def removeDuplicates(nums):
    nums[:]=sorted(set(nums))
    return len(nums)
#print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

def removeElement(nums,val):
    while val in nums:
        nums.remove(val)
    return len(nums)
#print(removeElement([0,1,2,2,3,0,4,2],2))

def searchInsert(nums,target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)
#print(searchInsert([1,3,5,6],5))

def maxSubArray(nums):
    newNum=maxTotal=nums[0]
    for i in range(1,len(nums)):
        newNum=max(nums[i], nums[i]+newNum)
        maxTotal=max(newNum,maxTotal)
    return maxTotal
#print(maxSubArray([5,4,-1,7,8]))