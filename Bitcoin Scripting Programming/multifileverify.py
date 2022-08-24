from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

#from lib.utils import *
#from lib.config import (my_private_key, my_public_key, my_address,
#                    faucet_address, network_type)
from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
import hashlib as hash
import math
#####################################
#####################################


num_of_leaves = input("Please enter the number of leaves :")
hash_of_leaves = []
for i in range(int(num_of_leaves)):
    x = input("Please enter your data :")
    hash_of_leaves.append(hash.sha256(x.encode('UTF-8')).digest())

power = math.ceil(math.log(int(num_of_leaves),2))
size = 2**power
for i in range (int(num_of_leaves),size):
    hash_of_leaves.append(hash_of_leaves[2*int(num_of_leaves)-(i+1)])

step = 1
for i in range(1,power+1):
    
    for j in range(0,int(size/2),step):
        hash_of_leaves[2*j]=hash.sha256(hash_of_leaves[2*j]+hash_of_leaves[step+2*j]).digest()
    step = i*2


merkle_root=hash_of_leaves[0]

########################
def P2PKH_scriptPubKey(address):
    #####################################   #################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [OP_DUP ,OP_HASH160 ,address, OP_EQUALVERIFY ,OP_CHECKSIG]
    #####################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [signature ,public_key]
    ######################################################################


pri_key = CBitcoinSecret.from_secret_bytes(merkle_root)
pub_key = pri_key.pub
address = P2PKHBitcoinAddress.from_pubkey(pub_key)



def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000001 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        'bab6271d531446d422b3494fa0b51d499eae56cd09ce0fb6bf4ede281fa601f2')
    utxo_index = 23 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)
