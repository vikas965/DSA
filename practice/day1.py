# 1. check password 

def CheckPassword(s):
    n=len(s)
    conditions =0
    if n<4:
        return 0
    if ord(s[0])>=48 and ord(s[0])<=57:
        return 0
    for i in s:
        if i==' ' or i=='/':
            return 0
    for i in s:
        if (ord(i)>=48 and ord(i)<=57):
            conditions+=1
            break
    for i in s:
        if (ord(i)>=65 and ord(i)<=90):
            conditions+=1
            break
    if conditions==2:
        return 1
    else:
        return 0


# check = 'aA_1'
# print(CheckPassword(check))


# 2. Calculate Binary operations 


def CalculateBinaryOperations(s):
    n=len(s)
    if n==0 or  n%2==0:
        return -1
    if n==1:
        return s[0]
    final = int(s[0])
    opr =s[1]
    for i in range(2,n,2):
        print(i)
        if opr=='A':            
            final=final&(int(s[i]))
        if opr=='B':
            final=final|(int(s[i]))
        if opr=='C':
            final=final^(int(s[i]))
        opr=s[i-1]
     
    return final


# stri ='1A0A1A1A1B1'
# print(CalculateBinaryOperations(stri))
    





# 3. differnceofsum

def differenceofSum(n,m):
    if n<=0 or m<=0:
        return -1
    
    div =0
    notdiv=0
    for i in range(1,m+1):
        if i%n==0:
            div+=i
        else:
            notdiv+=i
    return abs(div-notdiv)


# print(differenceofSum(3,10))


# 4. LargestSmallsum

def LargeSmallSum(arr):
    firstlarge =-999999999
    secondlarge = firstlarge
    firstsmall = 999999999
    secondsmall = firstsmall
    n=len(arr)
    for i in range(n):
        if i%2==0:
            if firstlarge<arr[i]:
                secondlarge=firstlarge
                firstlarge=arr[i]
            if(firstlarge>arr[i] and secondlarge<arr[i]):
                secondlarge=arr[i]
        else:
            if(firstsmall>arr[i]):
                secondsmall= firstsmall
                firstsmall=arr[i]
            if(firstsmall<arr[i] and secondsmall>arr[i]):
                secondsmall=arr[i]
   

    
    return secondlarge+secondsmall

arr=[1,8,0,2,3,5,6]
# print(LargeSmallSum(arr))






# 5.Rat Count House

def RatCountHouse(r,unit,arr):
    total = r*unit 
    n=len(arr)
    if n<=0:
        return -1
    for i in range(n):
        total-=arr[i]
        if total<=0:
            return i+1
    return 0


# arr=[2,8,3,5,7,4,1,2]
# print(RatCountHouse(7,2,arr))
    
    
    
