
import numpy as np

# Taking the range of the input
start = int(input("First Number: "))
end = int(input("Second Number: "))

# Initializing the vector
l = []
for i in range(start,end+1):
    l.append(i);
vector = np.array(l,dtype="float")
print("The initialized Vector is: "+str(vector))

## Creating the new Vector to be implemented on
vector_new = np.zeros((end-start+1)*5)

# Implementing the change
for i in range(0,vector_new.size,5):
    vector_new[i] = vector[i//5]
print("The new vector is: "+str(vector_new))