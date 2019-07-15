power=int(input())
flag=0
while power!=1:
    if power==0:
        print("no")
        flag=1
        break
    if power%2!=0:
        print("no")
        flag=1
        break
    power=power//2
if(flag==0):
    print("yes")

        
