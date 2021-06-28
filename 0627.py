def subtractProductAndSum(n):
    multi=1
    su=0
    n=str(n)
    for i in n:
        multi*=int(i)
        su+=int(i)
    return multi-su
#print(subtractProductAndSum(234))

def maximum69Number(num):
    a=list(str(num))
    for i in range(len(a)):
        if a[i]=='6':
            a[i]='9'
            break
    return int(''.join(a))
#print(maximum69Number(9969))

def sumBase(n,k):
    output=0
    while n:
        output+=(n%k)
        n//=k
    return output
#print(sumBase(34,6))

def diStirngMatch(s):
    n=len(s)
    result=[]
    initial=0
    final=n
    for i in range(n):
        if s[i]=='I':
            result.append(initial)
            initial+=1
        else:
            result.append(final)
            final-=1
    result.append(final)
    return result
#print(diStirngMatch('IDID'))

def smallestRange(nums,k):
    maxi=max(nums)
    mini=min(nums)
    return max(0,maxi-k-(mini+k))
#print(smallestRange([0,10],2))

def divisorGame(N):
    if N%2 == 1:
        return False
    else:
        return True
#print(divisorGame(5))

def addStrings(num1,num2):
    dic={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    n1,n2=0,0
    for c in num1:
        n1=n1*10+dic[c]
    for c in num2:
        n2=n2*10+dic[c]
    return str(n1+n2)
#print(addStrings('456','77'))

def isPowerOfTwo(n):
    while n>0:
        if n == 1:
            return True
        elif n%2==0:
            n=n/2
        else:
            return False
#print(isPowerOfTwo(3))

