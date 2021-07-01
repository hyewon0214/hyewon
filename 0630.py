def merge(nums1,m,nums2,n):
    return sorted(nums1[:m]+nums2[:n])
#print(merge([1,2,3,0,0,0],3,[2,5,6],3))

def isRectangleOverlap(rec1,rec2):
    width = min(rec1[2],rec2[2])-max(rec1[0],rec2[0])
    height=min(rec1[3],rec2[3])-max(rec1[1],rec2[1])
    return True if width>0 and height>0 else False

def dayOfYear(date):
    year,month,day = [int(i) for i in date.split('-')]
   # balance = 1 if (not year%4 and year%100 or not year%400) and month>2 else 0
    day_account=[0,31,59,90,120,181,212,243,273,304,334]
    return day_account[month-1]+day
#print(dayOfYear("2012-01-09"))

def countOdds(low,high):
    return (high+1)//2-(low//2)
#print(countOdds(3,7))

def rotateDigits(n):
    count = 0
    for d in range(1, n + 1):
        d = str(d)
        if '3' in d or '4' in d or '7' in d:
            continue
        if '2' in d or '5' in d or '6' in d or '9' in d:
            count += 1
    return count
#print(rotateDigits(10))

def titleToNumber(columnTitle):
    count=0
    for c in columnTitle:
        count= count*26+ord(c)-ord('A')+1
    return count
#print(titleToNumber('AB'))

def canWinWin(n):
    return n%4!=0
#print(canWinWin(1))

def isPerfectSquare(num):
    return int(num**0.5)==num**0.5
#print(isPerfectSquare(14))

def minMoves(nums):
    return sum(nums)-min(nums)*len(nums)

def largestTriangleArea(points):
    

