from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

#from lib.utils import *
#from lib.config import (my_private_key, my_public_key, my_address,
#                    faucet_address, network_type)
from utils import *
from config import *
 ##############################################################
def create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, seckey):
    tx = CMutableTransaction([txin], txout)                                    # txout is allredy a list
    sighash = SignatureHash(CScript(txin_scriptPubKey), tx,
                            0, SIGHASH_ALL)
    sig = seckey.sign(sighash) + bytes([SIGHASH_ALL])
    return sig

def create_signed_transaction(txin, txout, txin_scriptPubKey,
                              txin_scriptSig):
    tx = CMutableTransaction([txin], txout)   # txout is allredy a list
    txin.scriptSig = CScript(txin_scriptSig)
    VerifyScript(txin.scriptSig, CScript(txin_scriptPubKey),
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    return tx
 # #############################################################
                    

def P2PKH_scriptPubKey(address):
    #####################################   #################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    return [OP_DUP ,OP_HASH160 ,address, OP_EQUALVERIFY ,OP_CHECKSIG]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [signature ,public_key]
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = [create_txout(amount_to_send/3, txout_scriptPubKey)]*3

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey, # need t change due to the change of the txout
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,           # need t change due to the change of the txout
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.00000203 # amount of BTC in the output you're splitting minus fee
    txid_to_spend = (
        'bab6271d531446d422b3494fa0b51d499eae56cd09ce0fb6bf4ede281fa601f2')
    utxo_index = 25 # index of the output you are spending, indices start at 0
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
