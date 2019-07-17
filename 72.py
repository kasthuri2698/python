str=input()
count=0
for str1 in str:
    if str1=='a' or str1=='e' or str1=='i' or str1=='o' or str1=='u' or str1=='A' or str1=='E' or str1=='I' or str1=='O' or str1=='U':
       count=count+1
if count==0:
    print("no")
else:
    print("yes")
