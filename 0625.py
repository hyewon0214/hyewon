def isHappy(n):
    while n != 1:
        n=sum([int(i)**2 for i in str(n)])
        if n==4:
            return False
    return True
#print(isHappy(19))

def fizzBuzz(n):
    return ['FizzBuzz' if i%15==0 else 'Buzz' if i%5==0 else 'Fizz' if i%3==0 else str(i) for i in range(1,n+1)]
#print(fizzBuzz(5))

def truncateSentence(s,k):
    words=s.split(" ")
    return " ".join(words[0:k])
#print(truncateSentence("Hello how are you Contestant",4))

def solution(words):
    codes={"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
             "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
             "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
    res=set()
    for word in words:
        m=[]
        for ch in word:
            m.append(codes.get(ch))
        res.add("".join(m))
    return len(res)



