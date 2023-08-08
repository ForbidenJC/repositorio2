integers = [2,4,6,7,8]

def findOutlier(integers):
    numpar = None
    impar = None
    
    for num in integers:
        if num % 2 == 0:
            numpar = num
        else:
            impar = num
        
        if numpar is not None and impar is not None:
            break
    
    if numpar is not None:
        print(numpar)
    else:
        print(impar)