number=int(input())
sum=0
if number>0:
  digit=number%10
  sum=sum+digit
  num=num//10
print(sum)
