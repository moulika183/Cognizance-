impot numpy as np 
a = np.array([10,11,12,13,14])
print(a)
nz = 5
z = np.zeros(len(a) + (len(a)-1)*(nz))
z[::nz+1] = a
print()np.floor(z)]
