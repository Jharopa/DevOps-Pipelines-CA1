from Crypto.Cipher import DES

key = b'-8B key-'
cipher = DES.new(key, DES.MODE_OFB)
plain_text = b"Hello, World!"
message = cipher.iv + cipher.encrypt(plain_text)

print(message) 