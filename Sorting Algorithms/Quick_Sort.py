def quick_sort(data):
    le=len(data)
    
    if le==1:
        return [data[0]]
    
    elif le==2:
        if data[1]<data[0]:
            temp=data[0]
            data[0]=data[1]
            data[1]=temp
        return [data[0],data[1]]
    
    else:
        p=data[(le//2)]
        pivot=[]
        l=[]
        r=[]
        for i in data:
            if i<p:
                l.append(i)
            elif i>p:
                r.append(i)
            else:
                pivot.append(i)
        if len(l):
            l=quick_sort(l)
        if len(r):
            r=quick_sort(r)
        
        data=l+pivot+r
        return data
                
data=[-55,0,2,3,1,4,5,6,5,9,90]
data=quick_sort(data)
print(data)