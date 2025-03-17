def encrypt_caesar(plaintext, shift):
    """
    Encrypts the given plaintext using the Caesar cipher with the specified shift.

    Parameters:
    plaintext (str): The text to be encrypted.
    shift (int): The number of positions to shift each letter.

    Returns:
    str: The encrypted text.
    """
    result = ""
    for char in plaintext:
        if char.isupper():  # Check if the character is uppercase
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():  # Check if the character is lowercase
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def decrypt_caesar(ciphertext, shift):
    """
    Decrypts the given ciphertext using the Caesar cipher with the specified shift.

    Parameters:
    ciphertext (str): The text to be decrypted.
    shift (int): The number of positions to shift each letter back.

    Returns:
    str: The decrypted text.
    """
    result = ""
    for char in ciphertext:
        if char.isupper():  # Check if the character is uppercase
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():  # Check if the character is lowercase
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

def get_valid_shift():
    """
    Prompts the user for a valid shift value between 1 and 25.

    Returns:
    int: A valid shift value.
    """
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift  # Return the valid shift value
            else:
                print("Shift value must be between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def about_caesar():
    """
    Prints information about the Caesar cipher, including its history, how it works, and its limitations.
    """
    print("\nCaesar Cipher – History and Overview")
    print("The Caesar Cipher is one of the earliest and simplest encryption techniques. "
          "Named after Julius Caesar, who reportedly used it in military communication, "
          "this cipher involves shifting the letters of the alphabet by a fixed number of positions. "
          "Caesar is said to have used a shift of 3 to encode messages.\n")
    
    print("How It Works:")
    print("Each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.")
    print("For example, with a shift of 3:")
    print("A becomes D")
    print("B becomes E")
    print("C becomes F")
    print("...and so on.")
    print("For instance, the message 'HELLO' with a shift of 3 becomes 'KHOOR.'\n")
    
    print("Decryption:")
    print("To decrypt a message, the process is simply reversed, shifting the letters in the opposite direction by the same number.\n")
    
    print("Why It Was Used:")
    print("Simplicity: Caesar Cipher was simple and easy to implement, making it useful for military communication in Caesar's time.")
    print("Security: In ancient times, most people couldn't read or write, and very few had the tools to decrypt messages.\n")
    
    print("Historical Significance:")
    print("While rudimentary by today's standards, Caesar Cipher is significant in cryptography history because it introduced the concept of shifting alphabets to obscure a message.")
    print("It represents one of the first known applications of encryption and paved the way for more complex encryption techniques.\n")
    
    print("Limitations:")
    print("Vulnerable to Brute Force: Since there are only 25 possible shifts, it’s easy to break the cipher by trying all possible shifts.")
    print("Weak by Modern Standards: Modern encryption methods are far more secure and complex, whereas Caesar Cipher is too simple for secure communication today.")
    print("Despite its limitations, the Caesar Cipher remains a great educational tool to understand the basics of encryption.")

def menu():
    """
    Displays the menu for the user to choose between encrypting, decrypting, viewing information, or exiting.
    """
    while True:
        print("\nSelect an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. About Caesar Cipher")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            plaintext = input("Enter the message to encrypt: ")
            shift = get_valid_shift()
            encrypted_message = encrypt_caesar(plaintext, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == "2":
            ciphertext = input("Enter the message to decrypt: ")
            shift = get_valid_shift()
            decrypted_message = decrypt_caesar(ciphertext, shift)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == "3":
            about_caesar()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
