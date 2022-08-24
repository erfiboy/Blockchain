from sys import exit
from bitcoin.core.script import *
from utils import *
from config import *
                    
from ex1 import send_from_P2PKH_transaction

hamed_secretkey = CBitcoinSecret(
    'cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP')
hamed_publickey = hamed_secretkey.pub
hamed_address = P2PKHBitcoinAddress.from_pubkey(hamed_publickey)
######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q5a_txout_scriptPubKey = [
    1606925730, OP_CHECKLOCKTIMEVERIFY, OP_DROP, OP_DUP, OP_HASH160, hamed_address, OP_EQUALVERIFY, OP_CHECKSIG]
######################################################################


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000223 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        'bab6271d531446d422b3494fa0b51d499eae56cd09ce0fb6bf4ede281fa601f2')
    utxo_index = 10 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q5a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
