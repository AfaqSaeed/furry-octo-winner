 
## Good old basic recursion loop can give us the factorial without any major headches 
def factorials(n):
    
    if n!=0:
        fact = n*factorials(n-1) # function is called again and again with the main number getting reduced by one every time
    else :
        return 1 # return factorial of 0 as one which is the base case  
    return fact

x= factorials(100)

print("Factorial of 100 is :",x)
def sumdigits(fact): ## reduce the number by one order of magnitude each time it is called recursively 
    digit = fact%10 
    if (fact/10)>1:
        sum = digit + sumdigits(int(fact/10))
    else:
        return digit
    return sum 

print("Sum of digits in this factorail is :",sumdigits(x))

