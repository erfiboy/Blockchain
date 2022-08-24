from sys import exit
from bitcoin.core.script import *

from utils import *
from config import *

from ex1 import send_from_P2PKH_transaction

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q31a_txout_scriptPubKey = [OP_DUP, faraz_public_key, OP_CHECKSIG, OP_IF, OP_1, OP_ELSE, ata_public_key, OP_CHECKSIGVERIFY, OP_3,
    shar5_public_key, shar4_public_key, shar3_public_key, shar2_public_key, shar1_public_key,
    OP_5, OP_CHECKMULTISIG, OP_ENDIF]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000223 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('bab6271d531446d422b3494fa0b51d499eae56cd09ce0fb6bf4ede281fa601f2')
    utxo_index = 13 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, Q31a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
