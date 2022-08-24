from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from ex1 import P2PKH_scriptPubKey
from ex2a import Q2a_txout_scriptPubKey

#9710 - 2558 = 7152
######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00000023 # amount of BTC in the output you're splitting minus fee
txid_to_spend = (
        '46fb55edf873bcadaa7832d0f84d3a3575f1f939f7c3e3e2c4fe128343b0432d')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a. x = 8000 , y = 3000
x = 8000
y = 4000
txin_scriptSig = [x, y]
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
