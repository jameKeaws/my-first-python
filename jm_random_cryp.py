# Using cryptographic-appropriate methods to generate random data that may be sensitive
# secrets module introduced in Python 3.6
import os
import secrets


# TODO The urandom() function in the OS module produces random numbers 
# that are cryptographically safe to use for sensitive purposes
anyresult = os.urandom(8)
# print([hex(b) for b in anyresult])
    
# TODO secrets.choice is same to random.choice, but more secure
moves = ["rock", "paper", "scissors"]
# print(secrets.choice(moves))

# TODO secrets.token_bytes generates random bytes
token_bytes_result = secrets.token_bytes(8)
print(token_bytes_result)

# TODO secrets.token_hex creates a random string in hexadecimal
token_hex_result = secrets.token_hex(8)
print(token_hex_result)

# TODO secrets.token_urlsafe generates characters that can be in URLS 
urlsafe_result = secrets.token_urlsafe()
print(urlsafe_result)