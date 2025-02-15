from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Function to read binary file
def read_binary_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Read the key, IV, and ciphertext
key = read_binary_file("key.bin")
iv = read_binary_file("iv.bin")
ciphertext = read_binary_file("ciphertext.bin")

# Initialize AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt the ciphertext
plaintext = cipher.decrypt(ciphertext)

# Remove padding using PyCryptodome's unpad function
plaintext = unpad(plaintext, AES.block_size)

# Write the plaintext to a file
with open("paragraph.txt", "w", encoding="utf-8") as file:
    file.write(plaintext.decode("utf-8"))
