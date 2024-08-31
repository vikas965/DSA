

# fibonacci series  0 1 1 2 3 5 8 13 21
def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    # print(x)
    x = f(n-1)+f(n-2)
  
    return x
   

print(f(5))

