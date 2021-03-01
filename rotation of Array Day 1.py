arr=[2,5,6,7,9]
shift=3

def arrRotation(arr_1,shift):
    for i in range (0,shift):
        temp=arr_1[len(arr_1)-1]
        for j in range(len(arr_1)-1,0,-1):
            arr_1[j]=arr_1[j-1]
        arr_1[0]=temp
    return arr_1 

def printarray(array):
    for i in range(0,len(array)):
        print(array[i],end=' ')

x=arrRotation(arr,shift)
printarray(x)
print(x)