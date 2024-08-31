# sum of primes .......


# def sumofprimes(n):
#     arr =[]
#     for i in range(n+1):
#         arr.append(1)
#     z=int(n**(1/2))
#     for j in range(2,z+1):
#         if arr[j]:
#             for k in range(j*j,n+1,j):
#                 arr[k]=0
#     # print(arr)
#     totalsum=0
#     for m in range(2,n):
#         if(arr[m]):
#             totalsum+=m
    
#     return totalsum 


# print(sumofprimes(100))

    

def spiralorder(arr):
    result=[]
    top=0
    bottom=len(arr)-1
    left = 0
    right = len(arr[0])-1

    while top<=bottom and left<=right:
        for i in range(left,right+1):
            result.append(arr[top][i])
        top+=1

        for i in range(top , bottom+1):
            result.append(arr[i][right])
        right-=1

        if top<=bottom:
            for i in range(right ,left-1, -1):
                result.append(arr[bottom][i])
            bottom-=1

        if left<=right:
            for i in range(bottom ,top-1, -1):
                result.append(arr[i][left])
            left+=1
        
    print(result)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

spiralorder(matrix)
