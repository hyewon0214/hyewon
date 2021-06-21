def disStringMatch(s):
    n=len(s)
    result=[]
    initial=0
    final=n
    for i in range(n):
        if s[i]=='I':
            result.append(initial)
            initial=initial+1
        else:
            result.append(final)
            final=final-1
    result.append(final)
    return result
#print(disStringMatch('IDID'))

def defangIPaddr(address):
    n=''
    for i in address:
        if i == '.':
            n+='[.]'
        else:
            n+=i
    return n
print(defangIPaddr('1.1.1.1'))