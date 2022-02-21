a=int(input("Enter number:"))
temp=a
rev=0
while(a>0):
    num=a%10
    rev=rev*10+num
    a=a//10
if(temp==rev):
    print('True')
else:
    print('False')
