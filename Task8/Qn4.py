import pandas as pd
result=''
length=int(input("Enter The Length Of The Array:"))
statement=[input("Enter The Element:") for i in range(length)]
s_statement=pd.Series(statement)
for i in range(len(statement)):
    result+=(" "+s_statement[i])
print(result.title())
if length==statement:
    print("True")
