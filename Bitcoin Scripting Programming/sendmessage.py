from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
                    
from ex1 import send_from_P2PKH_transaction

input_string = input(" Please send your test: ").encode('UTF-8')
######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Qsm_txout_scriptPubKey = [ OP_RETURN ,input_string]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000000 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        'bab6271d531446d422b3494fa0b51d499eae56cd09ce0fb6bf4ede281fa601f2')
    utxo_index = 4 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Qsm_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
