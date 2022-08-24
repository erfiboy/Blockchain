from sys import exit
from bitcoin.core.script import *

from utils import *
from config import *

from ex1 import send_from_P2PKH_transaction
time = 1607097608
######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q6a_txout_scriptPubKey = [OP_2 , saeed_public_key , hamed_public_key , OP_2 , OP_CHECKMULTISIGVERIFY ,OP_1, OP_IF , OP_1 , OP_ELSE
                , 1607097608 , OP_CHECKLOCKTIMEVERIFY , saeed_private_key , OP_CHECKSIG ,OP_ENDIF]
    
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000223 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('bab6271d531446d422b3494fa0b51d499eae56cd09ce0fb6bf4ede281fa601f2')    
    utxo_index = 38 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, Q6a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)