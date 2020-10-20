
import numpy as np   
import math 
from sklearn.datasets import load_iris 
from sklearn import datasets, linear_model, metrics  
print("Umer Khyyam  17114156-069")

# load iris data set 
dataset = load_iris()    
a = dataset.data 
b = np.zeros(150) 
  
# take 1st column among 4 column of data set  
for i in range (150): 
    b[i]=a[i,1]    
  
b=np.sort(b)  #sort the array 
  
# create bins 
bin1=np.zeros((30,5))  
bin2=np.zeros((30,5)) 
bin3=np.zeros((30,5)) 
  
# Bin mean 
for i in range (0,150,5): 
    k=int(i/5) 
    mean=(b[i] + b[i+1] + b[i+2] + b[i+3] + b[i+4])/5
    for j in range(5): 
        bin1[k,j]=mean 
print("Bin Mean: \n",bin1) 
     
# Bin boundaries 
for i in range (0,150,5): 
    k=int(i/5) 
    for j in range (5): 
        if (b[i+j]-b[i]) < (b[i+4]-b[i+j]): 
            bin2[k,j]=b[i] 
        else: 
            bin2[k,j]=b[i+4]        
print("Bin Boundaries: \n",bin2) 
  
# Bin median 
for i in range (0,150,5): 
    k=int(i/5) 
    for j in range (5): 
        bin3[k,j]=b[i+2] 
print("Bin Median: \n",bin3) 
