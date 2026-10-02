# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    print("1")
    return 1
  elif n == 0:
    print("0")
    return 0 
  print("Recursion call with {0}".format(n))
  return fibonacci(n - 2) + fibonacci(n - 1)

fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"
