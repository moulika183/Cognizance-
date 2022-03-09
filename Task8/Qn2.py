import numpy as np
a=input("Enter The Array :").split()
a=np.array(list(map(int,a)))
b=input("Enter The Array :").split()
b=np.array(list(map(int,b)))
comparison = (a == b)
Condition= comparison.all()
if(Condition is True):
    print(True)
else:
    print(False)
