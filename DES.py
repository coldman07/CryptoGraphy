# Initial Permutation Table
IP = [58, 50, 42, 34, 26, 18, 10, 2, 
      60, 52, 44, 36, 28, 20, 12, 4, 
      62, 54, 46, 38, 30, 22, 14, 6, 
      64, 56, 48, 40, 32, 24, 16, 8, 
      57, 49, 41, 33, 25, 17, 9, 1, 
      59, 51, 43, 35, 27, 19, 11, 3, 
      61, 53, 45, 37, 29, 21, 13, 5, 
      63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation Table
FP = [40, 8, 48, 16, 56, 24, 64, 32, 
      39, 7, 47, 15, 55, 23, 63, 31, 
      38, 6, 46, 14, 54, 22, 62, 30, 
      37, 5, 45, 13, 53, 21, 61, 29, 
      36, 4, 44, 12, 52, 20, 60, 28, 
      35, 3, 43, 11, 51, 19, 59, 27, 
      34, 2, 42, 10, 50, 18, 58, 26, 
      33, 1, 41, 9, 49, 17, 57, 25]

# Expansion Table for the 32-bit right half
E = [32, 1, 2, 3, 4, 5, 4, 5, 
     6, 7, 8, 9, 8, 9, 10, 11, 
     12, 13, 12, 13, 14, 15, 16, 17, 
     16, 17, 18, 19, 20, 21, 20, 21, 
     22, 23, 24, 25, 24, 25, 26, 27, 
     28, 29, 28, 29, 30, 31, 32, 1]

# S-Boxes (simplified, S1 only; implement others similarly)
S_BOXES = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]


# Permutation P (after S-box)
P = [16, 7, 20, 21, 29, 12, 28, 17, 
     1, 15, 23, 26, 5, 18, 31, 10, 
     2, 8, 24, 14, 32, 27, 3, 9, 
     19, 13, 30, 6, 22, 11, 4, 25]

# Initial Permutation
def initial_permutation(block):
    return ''.join([block[i - 1] for i in IP])

# Final Permutation
def final_permutation(block):
    return ''.join([block[i - 1] for i in FP])

# Expansion of the 32-bit block to 48-bit
def expansion(right_half):
    return ''.join([right_half[i - 1] for i in E])

# Substitution using S-boxes
def sbox_substitution(xored_data):
    output = ""
    for i in range(8):  # There are 8 S-boxes
        block = xored_data[i * 6:(i + 1) * 6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        sbox_val = S_BOXES[i][row][col]
        output += format(sbox_val, '04b')
    return output

# Permutation after S-box substitution
def p_permutation(sbox_output):
    return ''.join([sbox_output[i - 1] for i in P])

# XOR function
def xor(bits1, bits2):
    return ''.join(['0' if bits1[i] == bits2[i] else '1' for i in range(len(bits1))])

# DES round function
def des_round(left, right, round_key):
    expanded_right = expansion(right)
    xored = xor(expanded_right, round_key)
    sbox_output = sbox_substitution(xored)
    permuted_output = p_permutation(sbox_output)
    new_right = xor(left, permuted_output)
    return new_right, right  # Swap for next round

# Key scheduling (just for example, simple shifts here)
def generate_round_keys(key):
    return [key[i:i + 48] for i in range(0, len(key), 48)]  # Simplified for this example

# DES encryption function
def des_encrypt(plain_text, key):
    # Convert plain text and key to binary
    plain_bin = ''.join(format(ord(c), '08b') for c in plain_text)
    key_bin = ''.join(format(ord(c), '08b') for c in key)

    # Initial permutation
    permuted_block = initial_permutation(plain_bin)

    # Split into two halves
    left, right = permuted_block[:32], permuted_block[32:]

    # Generate 16 round keys
    round_keys = generate_round_keys(key_bin)

    # Apply 16 rounds of DES
    for i in range(16):
        left, right = des_round(left, right, round_keys[i])

    # Combine halves and apply final permutation
    combined_block = right + left
    final_block = final_permutation(combined_block)

    # Convert binary back to text
    encrypted_text = ''.join(chr(int(final_block[i:i + 8], 2)) for i in range(0, len(final_block), 8))

    return encrypted_text

# DES decryption function (same process as encryption, just reverse the round keys)
def des_decrypt(cipher_text, key):
    # Convert cipher text and key to binary
    cipher_bin = ''.join(format(ord(c), '08b') for c in cipher_text)
    key_bin = ''.join(format(ord(c), '08b') for c in key)

    # Initial permutation
    permuted_block = initial_permutation(cipher_bin)

    # Split into two halves
    left, right = permuted_block[:32], permuted_block[32:]

    # Generate 16 round keys (reverse them for decryption)
    round_keys = generate_round_keys(key_bin)
    round_keys.reverse()

    # Apply 16 rounds of DES
    for i in range(16):
        left, right = des_round(left, right, round_keys[i])

    # Combine halves and apply final permutation
    combined_block = right + left
    final_block = final_permutation(combined_block)

    # Convert binary back to text
    decrypted_text = ''.join(chr(int(final_block[i:i + 8], 2)) for i in range(0, len(final_block), 8))

    return decrypted_text

# Menu Function
def des_menu():
    while True:
        print("\nDES Encryption Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plain_text = input("Enter plaintext (8 characters): ")
            key = input("Enter key (8 characters): ")
            if len(plain_text) != 8 or len(key) != 8:
                print("Both plaintext and key must be 8 characters!")
            else:
                encrypted_text = des_encrypt(plain_text, key)
                print("Encrypted Text:", encrypted_text)

        elif choice == '2':
            cipher_text = input("Enter ciphertext (8 characters): ")
            key = input("Enter key (8 characters): ")
            if len(cipher_text) != 8 or len(key) != 8:
                print("Both ciphertext and key must be 8 characters!")
            else:
                decrypted_text = des_decrypt(cipher_text, key)
                print("Decrypted Text:", decrypted_text)

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Start the DES menu
des_menu()
