# --------------
def palindrome(num):
    k=True
    
    
    
    while(k):
        num+=1
        p=str(num)
        if p[::]==p[::-1]:
            k=False
            return num


# --------------
#Code starts here
def a_scramble(str_1, str_2):
    k=""
    p=list(str_1.lower())
    o=list(str_2.lower())
    for i in range(len(o)):
        if (o[i] in p):
            k+=o[i]
            p.remove(o[i])
    return (len(k)==len(str_2))        



# --------------
#Code starts here
import math

# function to check perferct square
def checkPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    if pow(sqrt, 2) == n:
        return True
    else:
        return False

# function to check  Fibonacci number
def  check_fib(num):
    n=num
    res1 = 5 * n * n + 4
    res2 = 5 * n * n - 4
    if checkPerfectSquare(res1) or checkPerfectSquare(res2):
        return True
    else:
        return False


# --------------
#Code starts here
def compress(word):
    s=word.lower()
    if len(s) == 0:
        return None
    
    final_arr = []
    index = 0
    letter = s[0]
    
    for el in s:
        if el == letter and ord(el) == ord(letter):
            index += 1
        else: 
            final_arr.append(letter + repr(index))
            letter = el
            index = 1
            
    final_arr.append(letter + repr(index))       
    return "".join(final_arr)


# --------------
#Code starts here
def k_distinct(string,k):
   l=list(string.lower())
   b=set(l)  
   return  (len(b)==k)


