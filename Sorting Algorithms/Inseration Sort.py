def inseration_sort(data):
    l=len(data)
    dataresult=l*[None]
    for i in range(l):
        count=0
        for j in range(l):
            if data[j]<=data[i]:
                count+=1
        dataresult[count-1]=data[i]
    return dataresult

data=[2,3,1,6,0]
print(inseration_sort(data))