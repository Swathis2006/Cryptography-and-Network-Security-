text = input("Enter text: ")
key = input("Enter key: ")
choice = input("E for Encrypt / D for Decrypt: ").upper()

result = ""
k = 0

for ch in text.lower():
    if ch.isalpha():
        shift = ord(key[k % len(key)].lower()) - 97
        
        if choice == "E":
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += chr((ord(ch) - 97 - shift) % 26 + 97)
        
        k += 1
    else:
        result += ch

print("Result:", result)
