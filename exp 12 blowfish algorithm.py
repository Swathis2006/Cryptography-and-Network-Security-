from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

choice = int(input("Enter choice (1 Encrypt / 2 Decrypt): "))
key = input("Enter key: ").encode()

cipher = Blowfish.new(key, Blowfish.MODE_ECB)

if choice == 1:
    text = input("Enter text: ").encode()
    encrypted = cipher.encrypt(pad(text, Blowfish.block_size))
    print("Encrypted Text:", encrypted.hex())

elif choice == 2:
    text = bytes.fromhex(input("Enter encrypted text: "))
    decrypted = unpad(cipher.decrypt(text), Blowfish.block_size)
    print("Decrypted Text:", decrypted.decode())

else:
    print("Invalid choice")
