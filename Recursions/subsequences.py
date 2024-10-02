# First we will generate the subsequences of a string without recursion and using power set 

# for a string "abc" => the subsequences are a,b,c,ab,ac,bc,abc   if len ==n then no of 
# subsequnces are 2**n with including empty string " "


# To check whether i th bit of a number is set or not the condition is
# if  (n&(1<<i))!=0 then the bit is set 


# 0  & 0 0
#   0 0  & 1 0

def subseq(stri,n):
    a=(2**n)
    for i in range(a):
        sub=''
        for j in range(n):
            if(i&(1<<j)):
                # print(j,end=' ')
                sub+=stri[j]
        print(sub)
       

subseq('abc',3)
