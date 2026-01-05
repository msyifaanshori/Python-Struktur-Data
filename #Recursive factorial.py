#Recursive factorial
def faktorial(n):
  if n == 0:
    return 1
  else:
    return n * faktorial(n-1)

print(faktorial(3))
print(faktorial(4))
print(faktorial(5))

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

#recursive exponentiation
def pangkat(x,n):
  if n == 0:
    return 1
  else:
    return x * pangkat(x,n-1)

print(pangkat(2,3))
print(pangkat(3,3))
print(pangkat(4,3))

#fast exponentiation
def pangkat_cepat(x,n):
  if n == 0:
    return 1
  elif n % 2 == 0:
    return pangkat_cepat(x*x, n//2)
  else:
    return x * pangkat_cepat(x*x, (n-1)//2)

print(pangkat_cepat(2,3))

#recursive sum of a list
def sum_list(lst):
  if not lst:
    return 0
  else:
    return lst[0] + sum_list(lst[1:])

print(sum_list([1,2,3,4,5]))