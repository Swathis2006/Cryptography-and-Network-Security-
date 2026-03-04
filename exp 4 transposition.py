text = input("Enter text: ")
key = int(input("Enter key: "))
choice = input("E for Encrypt / D for Decrypt: ").upper()

result = ""

# -------- Encryption --------
if choice == "E":
    for i in range(key):
        result += text[i::key]

# -------- Decryption --------
elif choice == "D":
    n = len(text)
    rows = (n + key - 1) // key   # total rows

    cols = [""] * key
    start = 0

    for i in range(key):
        end = start + rows
        cols[i] = text[start:end]
        start = end

    for i in range(rows):
        for j in range(key):
            if i < len(cols[j]):
                result += cols[j][i]

print("Result:", result)
