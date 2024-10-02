

def oddeven(arr):
    result =''
    for i in arr:
        if i%2==0:
            result+='Even'
        else:
            result+='Odd'
    return result 


# print(oddeven([1,2,3,4,5,6]))

# def nofperms(s):
#     def fact(n):
#         f=1
#         for i in range(1,n+1):
#             f=f*i 
#         return f
#     dict = {}
#     vowels=['A','E','I','O','U','a','e','i','o','u']
#     for i in s:
#         if i not in vowels:
#             if i not in dict :
#                 dict[i]=1
#             else:
#                 dict[i]+=1 
#     total=0
#     denominator=1
#     for i in dict:
#         total+=dict[i]
#         if dict[i]>1:
#             denominator*=fact(dict[i])
#     numerator = fact(total)
#     return numerator//denominator


# print(nofperms('ABBCCC'))


def revevensum(arr):
    n=len(arr)
    index=0
    total=0
    for i in range(n-1,-1,-1):
        if index%2==0:
            total+=arr[i]
        index+=1
    return total


# arr=[21, 24, 67, 13, 24, 27]
# print(revevensum(arr))



        
# def playlist(s,k):
#     n=len(s)
#     maxcount=0
#     for i in range(n-k+1):
#         count=0
#         for j in range(i,i+k):
#             if s[j]=='a':
#                 count+=1
#         maxcount=max(maxcount,count)
#     return maxcount

# print(playlist('abcaca',3))



def equlibriumpoint(arr):
    n=len(arr)
    if n<3:
        return -1 
    left = arr[0]
    right = sum(arr[2:])
    for i in range(1,n-1):
        if left==right:
            return i 
        else:
            left +=arr[i]
            right-=arr[i+1]

        
    return -1
    
    
# print(equlibriumpoint([-7,1,5,-2,-4,0,0]))




def halfsort(arr):
    def rev(s,e,arr):
        while s<e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1 
    n=len(arr)
    rev(n//2,n-1,arr)
    print(arr)


# halfsort([1,2,3,4,5,6])



def abssumcount(arr,num,diff):
    count=0
    for i in arr:
        if abs(num-i)<=diff:
            count+=1
    if count==0:
        return -1
    return count 


# print(abssumcount([12,3,14,56,77,13],13,2))


def DectoNBase(num,n):
    s=''
    while(num):
        rem=num%n
        if(rem)<10:
            s+=str(rem)
        else:
            s+=chr(55+(rem))
        num=num//n
    print(s[::-1])

# DectoNBase(5678,21)





def noofcarries(num1,num2):
    total=0
    count=0
    carry=0
    while num1 and num2:
        val=carry +(num1%10)+(num2%10)
        total+=val%10
        carry=val//10
        if(carry!=0):
            count+=1
        num1=num1//10
        num2=num2//10
    while num1:
        val=carry +(num1%10)
        total+=val%10
        carry=val//10
        if(carry!=0):
            count+=1
        num1=num1//10
    while num2:
        val=carry +(num2%10)
        total+=val%10
        carry=val//10
        if(carry!=0):
            count+=1
        num2=num2//10

    return count


# print(noofcarries(990,10))



def sortedevenandarray(arr):
    n=len(arr)
    even=[]
    odd=[]
    for i in range(n):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    print(even)
    print(odd)


sortedevenandarray([3,4,1,7,9])


        



