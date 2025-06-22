# A simple text encryption exercise using the Caesar Cipher technique.
# The Caesar Cipher for `shift = 3` cyclically shifts every letter of the word by 3 positions:
# a -> d, b -> e, c -> f, ..., x -> a, y -> b, z -> c

def encrypt_text(text):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift = 3
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif char.islower():
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted

# Example text to encrypt
original_text = "Hello, Python!"
encrypted_text = encrypt_text(original_text)
print(encrypted_text)  # Expected output: Khoor, Sbwkrq!
