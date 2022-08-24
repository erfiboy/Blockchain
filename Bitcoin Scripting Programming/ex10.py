from bitcoin.core.script import *

######################################################################
# These functions will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
#
# TODO: Fill these in to create scripts that are redeemable by both
#       of the above conditions.
# See this page for opcode documentation: https://en.bitcoin.it/wiki/Script

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [OP_DUP,OP_HASH160 , hash_of_secret , OP_EQUAL , OP_IF , OP_DROP , OP_ELSE ,  public_key_sender, OP_CHECKSIGVERIFY,OP_ENDIF,
         public_key_recipient , OP_CHECKSIG]
        # fill this in!

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [sig_recipient , secret]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [sig_recipient , sig_sender ]
######################################################################

######################################################################
#
# Configured for your addresses
#
# TODO: Fill in all of these fields
#

alice_txid_to_spend     = "3a0d902dce1c1575ae3e69fcf54341279cd5988aecfe261d4e6077ddd84ff7a8"
alice_utxo_index        = 0
alice_amount_to_send    = 1000

bob_txid_to_spend       = "e9ab41b3e7f7169e6375e2ac653835f7ffc4fe5bbcfabf5a41a1a7a7b34dc571"
bob_utxo_index          = 0
bob_amount_to_send      = 1000

# Get current block height (for locktime) in 'height' parameter for each blockchain (and put it into swap.py):
#  curl https://api.blockcypher.com/v1/btc/test3
btc_test3_chain_height  = 1579945

#  curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height   = 2548698

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
## alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.0001

# While testing your code, you can edit these variables to see if your
# transaction can be broadcasted succesfully.
broadcast_transactions = False
alice_redeems = False

######################################################################
