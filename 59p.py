xx=int(input())
sum=0
if xx>0:
    digit=xx%10
    sum+=digit
    xx=xx//10
print(sum)
