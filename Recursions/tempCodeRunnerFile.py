def fun3(n,i):
    if i<1:
        return
    fun3(n,i-1)
    print(i)