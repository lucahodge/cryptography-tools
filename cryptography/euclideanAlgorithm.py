

def euclideanAlgo(a, b):
    if(a >= b):
        return euclideanHelper(a,b)
    else:
        return euclideanAlgo(b,a)

def euclideanHelper(a, b):
    if(b == 0):
        return a
    return euclideanAlgo(b, a%b)

def advancedEuclidean():
    return

print(euclideanAlgo(35,50))
print(euclideanAlgo(50,35))
print(euclideanAlgo(28358,24510))