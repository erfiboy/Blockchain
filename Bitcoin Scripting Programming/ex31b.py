from sys import exit
from bitcoin.core.script import *

from utils import *
from config import *

from ex1 import P2PKH_scriptPubKey
from ex31a import Q31a_txout_scriptPubKey

######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00000023 # amount of BTC in the output you're splitting minus fee
txid_to_spend = ('107041da1222ca5b3a8962981107f5b2a2c23c61589faa2f830f553840ec4897')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################
################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
txout = create_txout(amount_to_send, txout_scriptPubKey)
txin_scriptPubKey = Q31a_txout_scriptPubKey
txin = create_txin(txid_to_spend, utxo_index)
################################################################
faraz_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, faraz_private_key)
ata_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, ata_private_key)
shar1_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shar1_private_key)
shar2_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shar2_private_key)
shar3_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shar3_private_key)
shar4_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shar4_private_key)
shar5_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, shar5_private_key)
######################################################################

# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 31a.

txin_scriptSig = [faraz_signature]
######################################################################


response = send_from_custom_transaction(amount_to_send, txid_to_spend, utxo_index, txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
