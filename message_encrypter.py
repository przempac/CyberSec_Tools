from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message


if __name__ == "__main__":
    print("Welcome to the Python Encryption Tool!")

    while True:
        print("\nOptions:")
        print("1. Generate a new encryption key")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = generate_key()
            print(f"New encryption key generated: {key.decode()}")
        elif choice == "2":
            if 'key' not in locals():
                print("Please generate an encryption key first.")
                continue
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Encrypted message: {encrypted_message.decode()}")
        elif choice == "3":
            if 'key' not in locals():
                print("Please generate an encryption key first.")
                continue
            encrypted_message = input("Enter the encrypted message: ").encode()
            decrypted_message = decrypt_message(encrypted_message, key)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == "4":
            print("Exiting the Python Encryption Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
