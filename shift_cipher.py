# TODO: Define a function to encrypt the text using a shift cipher
def encrypt_text(text, shift):
# The function should take two parameters: the text to encrypt and the shift amount
    encrypt_text = ""

# TODO: Inside the function, create a loop that goes through each character of the text
    for char in text:

    # TODO: Check if the current character is an alphabetic character
        if char.isalpha():
           base = ord('A') if char.isupper() else ord('a')
        # TODO: Perform the character shift operation and append the result to the encrypted text
           shifted = (ord(char) - base + shift) % 26 + base
           encrypt_text += chr(shifted)
        else:
        # Hint: Use 'ord', 'chr', and modulo (%) operations to cyclically shift the letter by `shift`
             encrypt_text += char
    # TODO: If the character is not alphabetic, add it as is to the encrypted text
    return encrypt_text
# TODO: Outside the function, call your `encrypt_text` function with some sample text and a shift value to test it
sample_text = "Hello, World!"
shift_amount = 3
encrypted_result = encrypt_text(sample_text, shift_amount)
print("Original:", sample_text)
print("Encrypted:", encrypted_result)