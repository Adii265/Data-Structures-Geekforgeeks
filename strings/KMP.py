F = []
def prefix(P,m):
    i = 1
    j = 0
    F.insert(0,0)
    while(i<m):
        if P[i] == P[j]:
            F.insert(i,j+1)
            j+=1
            i+=1
        elif j>0:
            j = F[j-1]
        else:
            F.insert(i,0)
            i+=1
def action(T,n,P,m):
    i = 0
    j = 0
    prefix(P,m)
    while(i<n):
        if (P[j] == T[i]):
            if j == m-1:
                return i-j
            else:
                i+=1
                j+=1
        elif j>0:
            j = F[j-1]
        else:
            i+=1
    return -1
n = int(raw_input())
T = raw_input()
m = int(raw_input())
P = raw_input()
print("The string matched at position",action(T,n,P,m))
