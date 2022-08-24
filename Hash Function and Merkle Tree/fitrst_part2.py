import hashlib as hash
import math
import random
n = 2*math.ceil(math.sqrt(2*(2**20)*0.9))
numbers = []
hash_numbers = []
for i in range (n):
    numbers.append(str(random.randint(1,2**20)))
    hash_numbers.append(str(hex(int(hash.sha256(numbers[i].encode('UTF-8')).hexdigest() ,16) % (2**20))))
    if hash_numbers[i] in hash_numbers[:-1] and numbers[i] !=numbers[hash_numbers.index(hash_numbers[i], 0 , i-1 )]:
        print("this is the first number :" , numbers[i] )
        #print("it's hash is :" , format(int(hash_numbers[i],16) , "x" ))
        print("this is the second number : " , numbers[hash_numbers.index(hash_numbers[i], 0 , i-1 )])
        #print("it's hash is :" , format(int(hash_numbers[hash_numbers.index(hash_numbers[i], 0 , i-1 )],16),"x"))
        break