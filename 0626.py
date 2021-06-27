def twoSum(num, target):
    dic={}
    for i in range(len(num)):
        value=target-num[i]
        if value not in dic:
            dic[num[i]]=i
        elif value in dic:
            return [dic[value],i]
#print(twoSum([3,2,4],6))

def moveZeroes(nums):
    c=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[c],nums[i]=nums[i],nums[c]
            c+=1
    return nums
#print(moveZeroes([0,1,0,3,12]))

def findWords(words):
    return [x for x in words if set(x).issubset(set('qwertyuiopQWERTYUIOP'))or set(x).issubset(set("asdfghjklASDFGHJKL")) or set(x).issubset(set("zxcvbnmZXCVBNM"))]
#print(findWords(["Hello","Alaska","Dad","Peace"]))
    