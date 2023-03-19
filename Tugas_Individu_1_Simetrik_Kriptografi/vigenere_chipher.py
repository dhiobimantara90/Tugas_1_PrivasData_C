# Fungsi yang digunakan untuk mengenkripsi pesan dengan Vigenere cipher
def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            char = char.upper()
            # menghitung nilai shift berdasarkan huruf di key
            shift = ord(key[key_index % len(key)].upper()) - 65
            # Shift karakter berdasarkan nilai shift
            char = chr((ord(char) + shift - 65) % 26 + 65)
            key_index += 1
        ciphertext += char
    return ciphertext

# Fungsi untuk mendeskripsi pesan dengan Vigenere cipher
def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            # Hitung nilai shift sesuai huruf di key
            shift = ord(key[key_index % len(key)].upper()) - 65
            # Shift karakter sesuai nilai shift
            char = chr((ord(char) - shift - 65) % 26 + 65)
            # jangan lupa gunakan karakter key
            key_index += 1
        plaintext += char
    return plaintext

# Contoh penggunaan
plaintext = "Ini merupakan pesan yang benar eh tidak benar"
key = "245"
ciphertext = encrypt(plaintext, key)
print("Pesan terenkripsi:", ciphertext)
decrypted = decrypt(ciphertext, key)
print("Pesan didekripsi:", decrypted)