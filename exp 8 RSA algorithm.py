# Simple RSA Program

# Step 1: Choose small prime numbers
p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 3   # Public key (must be coprime with phi)

# Find d (private key)
for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break

print("Public Key (e,n):", (e, n))
print("Private Key (d,n):", (d, n))

choice = input("Enter E for Encrypt / D for Decrypt: ").upper()

# -------- Encryption --------
if choice == "E":
    msg = int(input("Enter number to encrypt: "))
    cipher = pow(msg, e, n)
    print("Encrypted message:", cipher)

# -------- Decryption --------
elif choice == "D":
    cipher = int(input("Enter number to decrypt: "))
    message = pow(cipher, d, n)
    print("Decrypted message:", message)

else:
    print("Invalid choice!")
