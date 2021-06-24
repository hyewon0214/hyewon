def searchInsert(nums,target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)
#print(searchInsert([1,3,5,6],6))

def majorityElement(nums):
    for num in set(nums):
        if nums.count(num)>len(nums)/2:
            return num
#print(majorityElement([1,1,1,1,2,2,3]))

def addDigits(num):
    if num < 10:
        return num
    else:
        return num%9
#print(addDigits(38))

def missingNumber(nums):
    return sum(range(len(nums)+1)) - sum(nums)
#print(missingNumber([3,0,1]))

def reverseString(s):
    return s[::-1]
#print(reverseString(["h","e","l","l","o"]))

def toGoartLatin(sentence):
    result=[]
    k=" "
    i=1
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for word in sentence.split(" "):
        if word[0] in vowel:
            word=word+'ma'
        else:
            word=word[1:] + word[0] + 'ma'
        word=word+'a'*i
        i=i+1
        result.append(word)
    return k.join(result)
print(toGoartLatin("I speak Goat Latin"))