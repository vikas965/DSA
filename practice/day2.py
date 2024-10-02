

# def OperationChoices(c,a,b):
#     if c==1:
#         return a+b 
#     elif c==2:
#         return a-b
#     elif c==3:
#         return a*b
#     elif c==4:
#         return a//b

# print(OperationChoices(1,25,5))
# print(OperationChoices(2,25,5))
# print(OperationChoices(3,25,5))
# print(OperationChoices(4,25,5))


# def ReplaceCharacter(s, n , ch1,ch2):
#     a=list(s)
#     if n==0:
#         return "NULL"
#     if ch1==ch2:
#         return "String is Unchanged"
#     ch1count =0
#     ch2count =0
#     for i in range(n):
#         if a[i]==ch1:
#             ch1count+=1
#             a[i]=ch2 
#         elif a[i]==ch2:
#             ch2count+=1
#             a[i]=ch1 
#     if ch1count==0 and ch2count==0:
#         return "String is Unchanged"

#     return ''.join(a)

# s='apples'
# ch1='z'
# ch2='y'
# n=len(s)
# print(ReplaceCharacter(s, n , ch1,ch2))



# def insertionsort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         temp = arr[i]
#         j=i-1
#         while j>-1  and temp<=arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=temp 

# arr=[9,6,5,0,2,1]
# print(arr)
# insertionsort(arr)
# print(arr)



# def countfrequencies(arr):
#     dict={}
#     for i in arr:
#         if  i not in dict:
#             dict[i]=1
#         else:
#             dict[i]+=1
    
#     for j in dict:
#         print(j,dict[j])

# arr=[10,20,20,10,10,20,5,20]
# countfrequencies(arr)



def removeDuplicates(arr):
        n=len(arr)
        i=0
        j=0
        while i<n and j<n:
            while(j<n and arr[i]==arr[j]):
                j+=1
            i+=1
            if j<n:
                arr[i]=arr[j]

        print(arr[:i])
       

       
# arr=[1,2,3,4,5,5,5,5,6,6]
# removeDuplicates(arr)


def checkodd(arr,l,r) :
        if r>=len(arr):
            return "error"
        if(arr[r]==1):
            return "odd"
        else:
            return "even"
      
arr=[1,1,0,1]
print(checkodd(arr,1,3))