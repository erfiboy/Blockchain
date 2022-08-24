import hashlib as hash
import math
num_of_leaves = input("Please enter the number of leaves :")
hash_of_leaves = []
for i in range(int(num_of_leaves)):
    x = input("Please enter your data :")
    hash_of_leaves.append(hash.sha256(x.encode('UTF-8')).hexdigest())

power = math.ceil(math.log(int(num_of_leaves),2))
size = 2**power
for i in range (int(num_of_leaves),size):
    hash_of_leaves.append(hash_of_leaves[2*int(num_of_leaves)-(i+1)])

step = 1
for i in range(1,power+1):
    
    for j in range(0,int(size/2),step):
        hash_of_leaves[2*j]=hash.sha256(hash_of_leaves[2*j].encode('UTF-8')+hash_of_leaves[step+2*j].encode('UTF-8')).hexdigest()
    step = i*2


print(hash_of_leaves[0])


        
