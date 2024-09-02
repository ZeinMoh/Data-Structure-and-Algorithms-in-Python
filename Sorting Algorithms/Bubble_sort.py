
def bubble_sort(data,c=False):
    l=len(data)
    sign=1
    if not c:
        sign=-1
    
    for i in range(l):
        for j in range(l):
            if data[i]*sign>data[j]*sign:
                temp=data[i]
                data[i]=data[j]
                data[j]=temp

data=[3,2,4,5]
bubble_sort(data,True)
print(data)