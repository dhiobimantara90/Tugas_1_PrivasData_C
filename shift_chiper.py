# Fungsi untuk mengenkripsi pesan dengan menggunakan Shift Cipher
def shift_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Digunakan untuk Mengkoversi karakter ke kode ASCII
            char_code = ord(char)
            # Shift sesuai jumlah karakter sebanyak key
            shifted_code = (char_code - 65 + key) % 26 + 65
            # dan akan di Konversi kembali ke karakter
            shifted_char = chr(shifted_code)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk mendekripsi pesan dengan menggunakan Shift Cipher
def shift_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Konversi karakter ke kode ASCII
            char_code = ord(char)
            # Shift karakter mundur sebanyak key
            shifted_code = (char_code - 65 - key) % 26 + 65
            # di Konversi kembali ke karakter
            shifted_char = chr(shifted_code)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan Shift Cipher
plaintext = "INI ADALAH DUA ANGKA NIM TERAKHIR SAYA 45"
key = 45
ciphertext = shift_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = shift_decrypt(ciphertext, key)
print("Plaintext:", decrypted_text)
