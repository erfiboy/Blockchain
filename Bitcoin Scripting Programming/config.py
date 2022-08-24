from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'btc-test3'


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/
# Adress : mppnKbNnwKCxkNgYCv6Fp3EhbDKqr8st3b
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
my_private_key = CBitcoinSecret(
    'cP2jUgShzKb5nVuduRYGtNtzZ3NQhAHvJcNnGRSbbZpBirUYpjW3')

my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!! # TXid 8b618c937d0a275a42cc3845bf266f07402970b3456bd4af6d38113db4427e56
alice_secret_key_BTC = CBitcoinSecret(
    'cSkddipDTZEdNAUcsV4H5eM3UjocSo5dQyNW6No6VRjCi5iA4TkG')
# Address mpZYGKu2SJw39V11qS7Senn3U1odJzcvZb
# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cR48N382C2xJH1n9DrXewG31ryZfbrjm2MzyYU4vf4gqSDnW5pM9')
# address mhhCY2Gj4aaxzVd3f7P8naPC2MxN6nhJAy
# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>
# This request will return a transaction reference. Make sure to save this.
    #curl -d "{\"addressn\": \"C4RH71vp9WpYkmqhSsWfGZp5VYjNfrN5Q1\", \"amount\": 1000000"} https://api.blockcypher.com/v1/bcy/test/faucet?token=150f18c4655d43a497214defa5db564b
# Only to be imported by alice.py

alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('3a0d902dce1c1575ae3e69fcf54341279cd5988aecfe261d4e6077ddd84ff7a8'))

#  6826c7fd8b7a46e1870df944075b8a99
#  "private": "3a0d902dce1c1575ae3e69fcf54341279cd5988aecfe261d4e6077ddd84ff7a8",
#  "public": "0348c2507b0e5c95ade5137fabaff687f0be21f2d069026d5d89dc7c9a3795767e",
#  "address": "BzFcxLZT4Nb5RXhxagB95QBMkSKSXTDBDy",
#  "wif": "BqGstU4zUN5TquG4RPP4Cz63ymyjX4w39G3v8dkdsMpBLgKMYfSY"
# Only to be imported by bob.py
# Bob should have coins!!

bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('e9ab41b3e7f7169e6375e2ac653835f7ffc4fe5bbcfabf5a41a1a7a7b34dc571'))

# 150f18c4655d43a497214defa5db564b
#"private": "e9ab41b3e7f7169e6375e2ac653835f7ffc4fe5bbcfabf5a41a1a7a7b34dc571",
#"public": "03fca04616212905ca07ebb659f4f9479a010346765415b95dc6d83feda6720f2c",
#"address": "C4RH71vp9WpYkmqhSsWfGZp5VYjNfrN5Q1",
#"wif": "BwAFcQZvuxnGthjkqT4MeYX4NdS98YwtDjGih9L2Lth8eSK645pZ"
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>
# "tx_ref": "14293bca8428488b302b05d39a316fbfb857b2b433f135c8d1cc082671b7b9a2"  10000
# "tx_ref": "6ecd3b47ed2f2dcfb5aae2b142167f8f3de91dc5f4b3bccbe22f8a564e8024d8"  1000000

# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
#Private key: cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP
#Address: mgZ66RLktzsmnc6qdUBBAtRk5jT3sSzHNj
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
faraz_private_key = CBitcoinSecret(
    'cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP')

faraz_public_key = faraz_private_key.pub
faraz_address = P2PKHBitcoinAddress.from_pubkey(faraz_public_key)
######################################################################


######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
#Private key: cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP
#Address: mgZ66RLktzsmnc6qdUBBAtRk5jT3sSzHNj
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
ata_private_key = CBitcoinSecret(
    'cP6g2dFzpfk9fiN6VdMLBdq1B8gcb2ESPnoQiKfPBNhG3gGWZAT9')

ata_public_key = ata_private_key.pub
ata_address = P2PKHBitcoinAddress.from_pubkey(ata_public_key)
######################################################################



######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
#Private key: cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP
#Address: mgZ66RLktzsmnc6qdUBBAtRk5jT3sSzHNj
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
shar1_private_key = CBitcoinSecret(
    'cQ27X4cQaFxUw7s54uYyUYGqKB4x5kMKBjRbM6MT1ECiNEdwZyvB')

shar1_public_key = shar1_private_key.pub
shar1_address = P2PKHBitcoinAddress.from_pubkey(shar1_public_key)
######################################################################

######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
#Private key: cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP
#Address: mgZ66RLktzsmnc6qdUBBAtRk5jT3sSzHNj
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
shar2_private_key = CBitcoinSecret(
    'cRYoxN6kveyG1FVSPWVuRoZqYp6QtwpZHfUGrTpWD23LSFVJeeff')

shar2_public_key = shar2_private_key.pub
shar2_address = P2PKHBitcoinAddress.from_pubkey(shar2_public_key)
######################################################################

######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
#Private key: cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP
#Address: mgZ66RLktzsmnc6qdUBBAtRk5jT3sSzHNj
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
shar3_private_key = CBitcoinSecret(
    'cSJo2PHRWCAzuAw58QUjbmZvur8VfdcodwHwFBKLbfSfoGM3VqnQ')

shar3_public_key = shar3_private_key.pub
shar3_address = P2PKHBitcoinAddress.from_pubkey(shar3_public_key)
######################################################################

######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
#Private key: cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP
#Address: mgZ66RLktzsmnc6qdUBBAtRk5jT3sSzHNj
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
shar4_private_key = CBitcoinSecret(
    'cP3mJbwSmNXJRnUwiJHKE7cyLwHVRHCVb96hJMtqBh9bCotbr6GQ')

shar4_public_key = shar4_private_key.pub
shar4_address = P2PKHBitcoinAddress.from_pubkey(shar4_public_key)
######################################################################

######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
#Private key: cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP
#Address: mgZ66RLktzsmnc6qdUBBAtRk5jT3sSzHNj
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
shar5_private_key = CBitcoinSecret(
    'cV7baqwRBaAoDV1wfnnXWRs1grYVPBjbqn1L6LQ9P1jNzrMeMDyF')

shar5_public_key = shar5_private_key.pub
shar5_address = P2PKHBitcoinAddress.from_pubkey(shar5_public_key)
######################################################################
######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
#Private key: cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP
#Address: mgZ66RLktzsmnc6qdUBBAtRk5jT3sSzHNj
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
saeed_private_key = CBitcoinSecret(
    'cNBVYuv3VifLJzyCNiASaFRrET4LiyST6y1pesN3owt87EW2qLyn')

saeed_public_key = saeed_private_key.pub
saeed_address = P2PKHBitcoinAddress.from_pubkey(saeed_public_key)
######################################################################
######################################################################
# This section is for Questions 1-3
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
#Private key: cQsSAgAUL5wLtW65freyTcsTd4TQkodhLQwMgQogDZjZ8Qga2JLP
#Address: mgZ66RLktzsmnc6qdUBBAtRk5jT3sSzHNj
# tx : f403ff2b6301fd03e3799712276d04426fdd4dbf92e401db795e149dfca2e199 
hamed_private_key = CBitcoinSecret(
    'cVPLqzExBqQM8MH98HiH6zE1U7iHADynRP4F1ojnjVAaxT9FbUiU')

hamed_public_key = hamed_private_key.pub
hamed_address = P2PKHBitcoinAddress.from_pubkey(hamed_public_key)
######################################################################

