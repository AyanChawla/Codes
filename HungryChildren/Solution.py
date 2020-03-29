# Write your code here
T=int(input())
stdnts=dict()
cnt=0
for i in range(T):
    j=input()
    #print(j)
    if j not in stdnts.keys(): 
        stdnts[j]=1
        
        #print(stdnts)
    else:
        #print("else",stdnts)
        #print(stdnts[j])
        if(stdnts[j]>i/2):
            #print("scold")
            cnt+=1
        stdnts[j]+=1
        #print("exit else",stdnts)
print(cnt)
#print(stdnts)
