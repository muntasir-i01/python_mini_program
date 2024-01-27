a = 2
b = 43
#swap
a, b = b, a
print(a, b)

#x = 9
#to evaluate single expression
sqr = lambda x:x*x
print(sqr)

#to input space seperated integers in a list
lis = list(map(int, input().split()))

#list comprehensions
evenNumbers = [x for x in range(11) if x%2==0]
    