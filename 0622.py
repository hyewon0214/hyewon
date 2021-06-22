def toLowerCase(s):
    return s.lower()
#print(toLowerCase('Hello'))

def countMatches(items,rulekey,ruleValue):
    count=0
    for a,b,c in items:
        if rulekey == 'type' and a == ruleValue:
            count+=1
        if rulekey == 'color' and b == ruleValue:
            count+=1
        if rulekey == 'name' and c == ruleValue:
            count+=1
    return count
#print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],'color','silver'))

def smallestRangeI(num,k):
    if len(num)==1:
        return 0
    else:
        mini=min(num)+k
        maxi=max(num)-k
        if mini>maxi:
            return 0
        else:
            return maxi-mini
print(smallestRangeI([0,10],2))