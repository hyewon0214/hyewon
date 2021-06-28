def defangIPaddr(address):
    a=""
    for i in address:
        if i == '.':
            a+='[.]'
        else:
            a+=i
    return a
#print(defangIPaddr('255.100.50.0'))

def numJewelISInStones(jewels,stones):
    return sum(stones.count(j) for j in jewels)
#print(numJewelISInStones('aA','aAAbbbb'))

def interpret(command):
    return command.replace('()','o').replace('(al)','al')
#print(interpret("G()()()()(al)"))

def balancedStringSplit(s):
    l,r=0,0
    for i in s:
        if i == 'R':
            l+=1
        else:
            l-=1
        if l == 0:
            r+=1
    return r
#print(balancedStringSplit("RLLLLRRRLR"))

def sortSentence(s):
    l=sorted(s.split(),key=lambda x:x[-1])
    return' '.join(w[:-1] for w in l)
#print(sortSentence("is2 sentence4 This1 a3"))

def checkIfPangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    counter=0
    output=True
    for i in alphabet:
        if i in sentence:
            counter+=1
            if counter == 26:
                output=True
            else:
                output = False
    return output
#print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

def arrayStringAreEqual(word1,word2):
    word1="".join(word1)
    word2="".join(word2)
    return word1==word2
#print(arrayStringAreEqual(["ab", "c"],["a", "bc"]))

def countConsistentString(allowed,words):
    allowed=set(allowed)
    count=0
    for word in words:
        for letter in word:
            if letter not in allowed:
                count += 1
                break
    return len(words)-count
#print(countConsistentString("ab",["ad","bd","aaab","baa","badab"]))

def truncateSentence(s,k):
    words=s.split(" ")
    return " ".join(words[0:k])

def removeOuterParentheses(S):
    res=""
    count=0
    first=0
    for i in range(len(S)):
        if S[i] == "(":
            count+=1
        else:
            count -=1
        if count ==0:
            res += (S[first+1:i])
            first = i+1
    return res
#print(removeOuterParentheses("(()())(())"))

def uniqueMorseRepresentations(words):
    code = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
            "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
            "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
            "z": "--.."}
    res=set()
    for word in words:
        m=[]
        for c in word:
            m.append(code.get(c))
        res.add("".join(m))
    return len(res)
#print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

def halvesAreAlike(s):
    vowels=set('aeiouAEIOU')
    count=0
    for i in range(len(s)//2):
        if s[i] in vowels:
            count+=1
        if s[-1-i] in vowels:
            count-=1
    return count ==0
#print(halvesAreAlike("MerryChristmas"))

def destCity(paths):
    d=dict(paths)
    for i in d.values():
        if i not in d.keys():
            return i
#print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))

def reverseOnlyLetters(S):
    l=[c for c in S if c.isalpha()]
    return "".join(l.pop() if c.isalpha() else c for c in S)
#print(reverseOnlyLetters("ab-cd"))

def isSubsequence(s,t):
    p1,p2=0,0
    while p1<len(s) and p2<len(t):
        if s[p1]==t[p2]:
            p1+=1
        p2+=1
    return p1==len(s)
#print(isSubsequence("abc","ahbgdc"))

def missingNumber(nums):
    return sum(range(len(nums)+1))-sum(nums)
#print(missingNumber([3,0,1]))

def smallestRangeI(nums,k):
    maxi=max(nums)
    mini=min(nums)
    return max(0,maxi-k-mini-k)
#print(smallestRangeI([0,10],2))

def generate(numRows):
    n,b,res=0,[1],[]
    while n<numRows:
        res.append(b)
        b=[1]+[b[i]+b[i+1] for i in range(len(b)-1)]+[1]
        n+=1
    return res
#print(generate(5))

def containDuplicate(nums):
    return len(nums)!=len(set(nums))
#print(containDuplicate([1,2,3,4]))

