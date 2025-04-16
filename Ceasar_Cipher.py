import os

def caesar_encrypt(plaintext, shift):
    """Encrypt plaintext using Caesar cipher with specified shift"""
    result = ""
    # For each character in the plaintext
    for char in plaintext:
        # Check if the character is a letter
        if char.isalpha():
            # Determine ASCII offset based on case (65 for uppercase, 97 for lowercase)
            ascii_offset = 65 if char.isupper() else 97
            # Apply the formula: (letter_position + shift) mod 26
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    """Decrypt ciphertext using Caesar cipher with specified shift"""
    # Decryption is just encryption with a negative shift
    return caesar_encrypt(ciphertext, -shift)

def print_caesar_history():
    """Print information about Caesar cipher history"""
    print("\n=== Caesar Cipher History ===")
    print("The Caesar cipher is one of the earliest known encryption techniques.")
    print("Key facts about Caesar cipher:")
    print("- Named after Julius Caesar, who used it in his private correspondence")
    print("- Caesar reportedly used a shift of 3 for his messages")
    print("- It's a substitution cipher where each letter is replaced by a letter some fixed number of positions down the alphabet")
    print("- Example: with a shift of 3, A becomes D, B becomes E, and so on")
    print("- Very simple to implement and use, but also very easy to break")
    print("- Offers only 25 possible keys (shifts), so it can be easily brute-forced")
    print("- In modern cryptography, it's used as an educational tool rather than for secure communication")
    print("- Forms the basis for more complex ciphers like the Vigenère cipher")
    print("=========================\n")

def display_banner():
    """Display a banner with CAESAR-CIPHER text"""
    # Clear screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')
    
    banner = """
    ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗        ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗      ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
    ██║     ███████║█████╗  ███████╗███████║██████╔╝█████╗██║     ██║██████╔╝███████║█████╗  ██████╔╝
    ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗╚════╝██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
    ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║      ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
     ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                             -madeby: ColdMan[Vibhu]
    """
    print(banner)

def display_menu():
    """Display the banner and menu"""
    display_banner()
    print("\n=== Caesar Cipher Program ===")
    
    print("\nMenu:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. About Caesar cipher history")
    print("4. Exit")

def main():
    while True:
        # Display banner and menu each time
        display_menu()
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            plaintext = input("Enter the message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("\nInvalid shift value. Please enter a number between 1 and 25.")
                else:
                    encrypted = caesar_encrypt(plaintext, shift)
                    print(f"\nEncrypted message: {encrypted}")
            except ValueError:
                print("\nInvalid input. Shift must be a number.")
            input("\nPress Enter to continue...")
            
        elif choice == '2':
            ciphertext = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("\nInvalid shift value. Please enter a number between 1 and 25.")
                else:
                    decrypted = caesar_decrypt(ciphertext, shift)
                    print(f"\nDecrypted message: {decrypted}")
            except ValueError:
                print("\nInvalid input. Shift must be a number.")
            input("\nPress Enter to continue...")
            
        elif choice == '3':
            print_caesar_history()
            input("\nPress Enter to continue...")
            
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
