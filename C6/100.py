import math

def nested_sqrt(a, n):
  result = 0
  for i in range(1,n + 1):
    result = math.sqrt(result + a)
  return result

a = 2
n = int(input("Input n: "))


result = nested_sqrt(2, n)
print(f"The result of the nested square root expression {n} times of 2 is: {result}")