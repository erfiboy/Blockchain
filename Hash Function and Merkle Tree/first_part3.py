import hashlib as hash
import math
import random

def sender (massage , s):   
    concat_massage = massage + s
    hash_massage = hash.sha256(concat_massage.encode('UTF-8')).hexdigest()
    output = [massage , hash_massage]
    return output

def receiver (sent_massage , s):
    concat_massage = sent_massage[0] + s
    hash_massage = hash.sha256(concat_massage.encode('UTF-8')).hexdigest()
    if hash_massage == sent_massage[1]:
        print(sent_massage[0])
    else:
        print("The message has been changed!")



m = "salam !!!"
s = "sdfadfsa"  
receiver(sender(m,s),s)