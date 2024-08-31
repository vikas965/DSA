# reverse an array  , without recursion we can reverse an array basically using the two pointer
# approach same concept we will apply here to reverse an array using recusrion


def revarr(arr,l,r):
    if l>r:
        return 
    arr[l],arr[r]=arr[r],arr[l]
    revarr(arr,l+1,r-1)

arr=[1,2,3,4,5,6]
n=6
revarr(arr,0,n-1)
print(arr)



# check whether a string is a plaindrome or not using recursion


def strfun(inpstr,l,r):
    if l>=r:
        print(True)
        return 
    if inpstr[l]!=inpstr[r]:
        print(False)
        return
    strfun(inpstr,l+1,r-1)


inpstr = "madam"
l=0
r=5
strfun(inpstr,l,r-1)


