def longestCommonPrefix(strs):
    result=[]
    for s in zip(*strs):
        if len(set(s))!=1:
            break
        result.append(s[0])
    return "".join(result)
#print(longestCommonPrefix(["flower","flow","flight"]))

def isValid(s):
    while len(s)>0:
        l=len(s)
        s=s.replace('()','').replace('{}','').replace('[]','')
        if l==len(s): return False
    return True
#print(isValid("([)]"))

def isPalindrome(s):
    newS=[i.lower() for i in s if i.isalnum()]
    return newS==newS[::-1]
#print(isPalindrome("A man, a plan, a canal: Panama"))

def titleToNumber(columnTitle):
    count=0
    for c in columnTitle:
        count=count*26+ord(c)-ord('A')+1
    return count

def isAnagram(s,t):
    return sorted(s)==sorted(t)
#print(isAnagram("anagram","nagaram"))

