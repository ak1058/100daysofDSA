num=[1,2,3,4,5,6,7,8]
shift=2
def reverseArray(arr_1,len(arr_1)):
    for i in arr_1:
        temp=arr_1[i]
        arr_1[i]=arr_1[len(arr_1)-1]
        arr_1[len(arr_1)-1]=temp
        i=+1
        len(arr_1)=len(arr_1)-1


def arrRotation(arr,shift):
    reverseArray(arr,shift)
    reverseArray()        
x=arrRotation(num)
print(x)