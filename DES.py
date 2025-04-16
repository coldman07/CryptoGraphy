import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def pad(data):
    """Pad the data to a multiple of 8 bytes (DES block size)"""
    padding_length = 8 - (len(data) % 8)
    padding = bytes([padding_length]) * padding_length
    return data + padding

def unpad(data):
    """Remove padding from the data"""
    padding_length = data[-1]
    return data[:-padding_length]

def generate_key():
    """Generate a random 8-byte (64-bit) DES key"""
    return os.urandom(8)

def encrypt_des(plaintext, key):
    """Encrypt plaintext using DES"""
    # Convert string to bytes if needed
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # Pad the plaintext to a multiple of 8 bytes
    padded_plaintext = pad(plaintext)
    
    # Create the cipher object - using TripleDES with same key for all parts
    cipher = Cipher(algorithms.TripleDES(key + key[:8] + key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    # Encode the ciphertext to base64 for readability
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_des(ciphertext, key):
    """Decrypt ciphertext using DES"""
    # Decode the base64-encoded ciphertext
    ciphertext_bytes = base64.b64decode(ciphertext)
    
    # Create the cipher object - using TripleDES with same key for all parts
    cipher = Cipher(algorithms.TripleDES(key + key[:8] + key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(ciphertext_bytes) + decryptor.finalize()
    
    # Remove padding and return the plaintext
    plaintext = unpad(padded_plaintext)
    return plaintext.decode('utf-8')

def print_des_history():
    """Print information about DES cipher history"""
    print("\n=== DES Cipher History ===")
    print("DES (Data Encryption Standard) was developed in the early 1970s at IBM.")
    print("Key facts about DES:")
    print("- Originally published as FIPS PUB 46 in 1977 by the US National Bureau of Standards")
    print("- Based on the Lucifer cipher developed by Horst Feistel at IBM")
    print("- Uses a 56-bit key (technically 64 bits, but 8 bits are used for parity checks)")
    print("- Operates on 64-bit blocks of data")
    print("- Employs a Feistel network structure with 16 rounds")
    print("- By the late 1990s, DES was considered insecure due to its small key size")
    print("- In 1999, a DES key was cracked in less than 24 hours")
    print("- Replaced by Triple DES (3DES) and later AES (Advanced Encryption Standard)")
    print("- Despite being deprecated, DES was influential in the development of modern cryptography")
    print("- No longer considered secure for sensitive data in its original form")
    print("=========================\n")

def display_banner():
    """Display a banner with DES-Cipher text"""
    # Clear screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = """
    ██████╗ ███████╗███████╗       ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔════╝██╔════╝      ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
    ██║  ██║█████╗  ███████╗█████╗██║     ██║██████╔╝███████║█████╗  ██████╔╝
    ██║  ██║██╔══╝  ╚════██║╚════╝██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
    ██████╔╝███████╗███████║      ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
    ╚═════╝ ╚══════╝╚══════╝       ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                                        -madeby: ColdMan[Vibhu]
    """
    print(banner)

def display_menu(key):
    """Display the banner and menu"""
    display_banner()
    print("\n=== DES Encryption Program ===")
    print(f"Current key (base64): {base64.b64encode(key).decode('utf-8')}")
    
    print("\nMenu:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. About DES cipher history")
    print("4. Exit")

def main():
    # Generate a key (in a real application, you would want to save this securely)
    key = generate_key()
    
    while True:
        # Display banner and menu each time
        display_menu(key)
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            plaintext = input("Enter the message to encrypt: ")
            encrypted = encrypt_des(plaintext, key)
            print(f"\nEncrypted message: {encrypted}")
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            ciphertext = input("Enter the encrypted message (base64): ")
            try:
                decrypted = decrypt_des(ciphertext, key)
                print(f"\nDecrypted message: {decrypted}")
            except Exception as e:
                print(f"\nError decrypting message: {e}")
                print("Make sure you're using the correct key and the message is properly formatted.")
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            print_des_history()
            input("\nPress Enter to continue...")
            
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
