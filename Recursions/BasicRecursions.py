# without backtracking  means we will print any value before calling the inner function
# here the values will be printed will stack was pushing
#fun1  1 to n  

#fun2 n to 1

# def fun1(n,i):
#     if i>n:
#         return
#     print(i)
#     fun1(n,i+1)

# def fun2(n,i):
#     if n<i:
#         return
#     print(n)
#     fun2(n-1,i)

# fun1(5,1)
# fun2(5,1)



# with backtracking  means we will print any value after calling the inner function   
# here the values will be printed will stack was poping



def fun3(n,i):
    if i<1:
        return
    fun3(n,i-1)
    print(i)
    

def fun4(i,n):
    if i>n:
        return
    fun4(i+1,n)
    print(i)
    

fun3(5,5)
fun4(1,5)