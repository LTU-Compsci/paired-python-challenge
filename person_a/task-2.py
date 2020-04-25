# Task 2: Decrypt your partner's mystery message...
from cryptography.fernet import Fernet

key = b'SbeDLkiwE9SW-W5QDq7J-PT9hgILOnonl1Ujj3xYz14='
cipher_suite = Fernet(key)

cipher_text = cipher_suite.encrypt(b'a secret message')

plain_text = cipher_suite.decrypt(cipher_text)

# Stuck? Want more info?
# https://docs.python-guide.org/scenarios/crypto/

