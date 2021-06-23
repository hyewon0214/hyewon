def halvesAreAlike(s):
    vowels=set('aeiouAEIOU')
    count=0
    for i in range(len(s)//2):
        if s[i] in vowels:
            count+=1
        if s[-1-i] in vowels:
            count+=1
        return count==0
   #vowels=set('aeiouAEIOU')
   #a,b=0,0
   #for i in range(len(s)//2):
   #    if s[i] in vowels:
   #        a+=1
   #    if s[-1-i] in vowels:
   #        b+=1
   #return a==b
#print(halvesAreAlike('book'))


def removeElement(nums,val):
    while val in nums:
        nums.remove(val)
    return len(nums)
#print(removeElement([0,1,2,2,3,0,4,2],2))