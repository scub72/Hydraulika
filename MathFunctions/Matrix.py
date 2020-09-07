
def sumList(A, B):

    C=[]
    if len(A)==len(B):
        for i in range(0,len(A),1):
            C.append(A[i]+B[i])
        return C
    else:
        print "Wrong size of list cannot sum"

def sumTwoDimensionArray(A,B):

    C = []
    if len(A) == len(B):
        for i in range(0, len(A), 1):
            C2 = []
            if len(A[i]) == len(B[i]):
                for j in range(0, len(A[i]), 1):
                    A2=A[i]
                    B2=B[i]
                    C2.append(A2+B2)

            C.append(C2)
        return C
    else:
        print "Wrong size of Matrix cannot sum"

