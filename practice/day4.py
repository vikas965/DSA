# Minimum Unfairness


def minimumunfair(arr,k):
    n=len(arr)
    arr.sort()
    finalans =99999
    for i in range(n-k+1):
        sub= arr[i:i+k]
        if(finalans>sub[2]-sub[0]):
            finalans=sub[2]-sub[0]
    print(finalans)




# minimumunfair([10,100,99,98,300,200,1000,20,30,1,4,10],3)





def noofdigits(num1,num2):
    arr1=[]
    arr2=[]
    for i in range(10):
        arr1.append(0)
        arr2.append(0)
    while(num1):
        arr1[num1%10]+=1
        num1=num1//10
    while(num2):
        arr2[num2%10]+=1
        num2=num2//10
    count =0
    for i in range(10):
        if arr1[i]>0 and arr2[i]>0:
            count+=1

    return count 


# print(noofdigits(748294,34298156))





# def fib(n):
#     n1=0
#     n2=1
#     for i in range(n+1):
#         n3=n1+n2
#         n1=n2
#         n2=n3 
#     print(n3)

# fib(5)



def autobio(num):
    arr=[]
    new =[]
    for i in range(10):
        arr.append(0)
    while(num):
        arr[num%10]+=1
        new.append(num%10)
        num=num//10
    index=0
    for i in new[::-1]:    
        if i!=arr[index]:
            return False
        index+=1
    return True

print(autobio(20208))
    