# This function calculates factorial using recursion
def	factorial_recursive(n):
      if n==0 or n==1:
          return 1
      else:
          return n*factorial_recursive(n-1)

num = int(input("Enter the number:")) 
print("Factorial of number",factorial_recursive(num))