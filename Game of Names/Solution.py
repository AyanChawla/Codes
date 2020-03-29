# Write your code here
n=int(input())
b=[]
flg=0
for i in range(n):
    a=input()
    b.append(a)
#HORIZONTAL
for i in range(n):
    for j in range(n-2): 
        #print(b[i][j],b[i][j+1],b[i][j+2])
        if (b[i][j]==b[i][j+1] and b[i][j]==b[i][j+2] and b[i][j]!='.'):
            print(b[i][j])
            flg=1
#VERTICAL
for i in range(n-2):
    for j in range(n):
        #print(b[i][j],b[i+1][j],b[i+2][j])
        if (b[i+1][j]==b[i][j]and b[i+2][j]==b[i][j] and b[i][j]!='.'):
            print(b[i][j])
            flg=1
# POSITIVE SLOPES DIAGONAL
for i in range(n-2):
    for j in range(n-2):
        #print(b[i][j],b[i+1][j+1],b[i+2][j+2])
        if (b[i][j]==b[i+1][j+1]and b[i][j]==b[i+2][j+2] and b[i][j]!='.'):
            print(b[i][j])
            flg=1

# NEGATIVE SLOPES DIAGONAL
for i in range(2,n):
    for j in range(n-2):
        #print(b[i][j],b[i-1][j+1],b[i-2][j+2])
        if (b[i][j]==b[i-1][j+1]and b[i][j]==b[i-2][j+2] and b[i][j]!='.'):
            print(b[i][j])
            flg=1
if (flg==0):
    print("ongoing")
