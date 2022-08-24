from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

#from lib.utils import *
#from lib.config import (my_private_key, my_public_key, my_address,
#                    faucet_address, network_type)
from utils import *
from config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)



def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################

def create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, seckey, index):
    tx = CMutableTransaction(txin, [txout])
    sighash = SignatureHash(CScript(txin_scriptPubKey), tx,
                            index, SIGHASH_ALL)
    sig = seckey.sign(sighash) + bytes([SIGHASH_ALL])
    return sig

def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    txin_scriptSig = list([])
    index = 0
    for i in txin:
        signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, private_key, index)
        txin_scriptSig.append([signature, public_key])
        index = index + 1
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return txin_scriptSig
    ######################################################################

def create_signed_transaction(txin, txout, txin_scriptPubKey,
                              txin_scriptSig):
    tx = CMutableTransaction(txin, [txout])
    index = 0
    for i in txin:
        i.scriptSig = CScript(txin_scriptSig[index])
        VerifyScript(i.scriptSig, CScript(txin_scriptPubKey),
                    tx, index, (SCRIPT_VERIFY_P2SH,))
        index = index + 1
    return tx

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
    txin = [create_txin(txid_to_spend , utxo_index[0]), create_txin(txid_to_spend , utxo_index[1]) ,create_txin(txid_to_spend , utxo_index[2]) ]
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey, sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey, txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000003 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        'bab6271d531446d422b3494fa0b51d499eae56cd09ce0fb6bf4ede281fa601f2')
    utxo_index = [28,29,30] # index of the output you are spending, indices start at 0
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
