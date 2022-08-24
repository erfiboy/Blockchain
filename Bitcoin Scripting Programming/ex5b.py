from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from utils import *
from config import *
from ex1 import (P2PKH_scriptPubKey,P2PKH_scriptSig,send_from_P2PKH_transaction)
from ex5a import (hamed_secretkey, hamed_publickey, Q5a_txout_scriptPubKey)

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = Q5a_txout_scriptPubKey
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = hamedsig_scriptSig(txin, txout, txin_scriptPubKey,hamed_secretkey, hamed_publickey)
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)






def hamedsig_scriptSig(txin, txout, txin_scriptPubKey,hamed_secretkey, hamed_publickey):
    hamed_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             hamed_secretkey)
    return [hamed_signature , hamed_publickey]

######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00000023 # amount of BTC in the output you're splitting minus fee
txid_to_spend = (
        'd97c9f8289ec67075f150f30348120e66074babd102da3e5b807f9ad8b79280e')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q5a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a. x = 8000 , y = 3000

######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_P2PKH_transaction(
    amount_to_send,
    txid_to_spend,
    utxo_index,
    txout_scriptPubKey,
    hamed_secretkey,
    network_type,
)
print(response.status_code, response.reason)
print(response.text)
