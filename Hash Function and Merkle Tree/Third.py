import hashlib as hash
import math
num_of_leaves = input("Please enter the number of leaves :")
k = int(input("which document do you want to check :"))
power = math.ceil(math.log(int(num_of_leaves),2))
size = 2**power
data = []
root = []
for i in range(power+2):
    if i == 0 :
        data.append(hash.sha256(input("Please enter your data :").encode('UTF-8')).hexdigest())
    elif i == (power+1):
        root.append(input("please enter your root :"))
    else:
        data.append(input("please enter your layer %d hash :" %i))
flag = (k % 2) + 1
for i in range (power):
    if flag :
        data[i+1]=hash.sha256(data[i+1].encode('UTF-8')+data[i].encode('UTF-8')).hexdigest()
        flag = 0
    else:
        data[i+1]=hash.sha256(data[i].encode('UTF-8')+data[i+1].encode('UTF-8')).hexdigest()
        flag = 1

if data[power] == root[0] :
    print("Existed") 
else:
    print("Did not exist!")