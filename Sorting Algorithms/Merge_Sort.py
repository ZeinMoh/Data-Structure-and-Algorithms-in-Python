def merge(left, right):
    merged = []
    il, ir = 0, 0
    ll, rr = len(left), len(right)

    while il < ll and ir < rr:
        if left[il] < right[ir]:
            merged.append(left[il])
            il += 1
        else:
            merged.append(right[ir])
            ir += 1

    while il < ll:
        merged.append(left[il])
        il += 1

    while ir < rr:
        merged.append(right[ir])
        ir += 1

    return merged

def merge_sort(data):
    le=len(data)
    
    if le==1:
        
        return [data[0]]
    
    elif le==2:
        if data[0]>data[1]:
            return [data[1],data[0]]
        else:
            return data
        
    else:
        l=[]
        r=[]
        
        l=data[:le//2]
        r=data[(le//2):]

        if len(l):
            l=merge_sort(l)
        if len(r):
            r=merge_sort(r)
      
        return merge(l,r)

    
data=[2,3,1,5,0]
print(merge_sort(data))
