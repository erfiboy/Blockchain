import hashlib as hash
import math
my_id = "97102558"
print("my id is : " , my_id)
mod = 2**20
hash_of_my_id = hex(int(hash.sha256(my_id.encode('UTF-8')).hexdigest() ,16) % (2**20))
for i in range (2**20):
    x = hex(int(hash.sha256(str(i).encode('UTF-8')).hexdigest()  , 16) % (2**20))
    if x == hash_of_my_id and i != 97102558 :
       print("hash of my student number is :" ,format(int(hash_of_my_id , 16 ) , "x"))
       print("the random number is :" ,i)
       print("hash of the random number is :",format(int(x,16) , "x"))
       t = i
       break


