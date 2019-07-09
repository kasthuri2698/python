num=int(input())
sum=0
temp=num
while temp>0:
  digt=temp%10
  sum +=digt**3
  temp=temp//10
if temp==sum:
  print("yes")
else:
  print("no")
