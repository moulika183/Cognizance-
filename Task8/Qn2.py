import numpy as np
l1 = []
n1 = int(input("size of the list : "))
for i in range(n1):
    l1.append(int(input("enter the first array : ")))
l2 = []
for i in range(n1):
    l2.append(int(input("enter the second array : ")))
y = np.array(l1)
x = np.array(l2)
a = np.allclose(x,y)
print("first array :")
print(l1)
print("second array :")
print(l2)
print(a)
