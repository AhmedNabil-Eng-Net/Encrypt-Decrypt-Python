
# ---------- # -- 🔐 Encrypt & Decrypt in Python -- # ---------- #

import os
import random
import string
import time

from colorama import Fore, Style, init


# Clear the console screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Display the main menu
def show_menu():
    print("1. Encrypt a text 🔐")
    print("2. Decrypt a text 🔓")
    print("3. Show key 🔑")
    print("4. Save key 💾")
    print("5. Load key 📂")
    print("6. Generate New Key 🔄")
    print("7. Exit 🚪")


# Encrypt the given text using the current encryption key
def encrypt(text, chars, encryption_key):
    encrypted_text = []

    for char in text:
        if char in chars:
            encrypted_text.append(encryption_key[char])
        else:
            # Keep unsupported characters unchanged
            print(
                f'{Fore.RED}Character "{char}": Not supported; '
                f'{Style.RESET_ALL}it will remain as it is.'
            )
            encrypted_text.append(char)

    print(
        f'-> 🔐 Encrypted Text: '
        f'[{Fore.GREEN}{"".join(encrypted_text)}{Style.RESET_ALL}]'
    )


# Decrypt the given text using the current decryption key
def decrypt(text, keys, decryption_key):
    decrypted_text = []

    for char in text:
        if char in keys:
            decrypted_text.append(decryption_key[char])
        else:
            # Keep unsupported characters unchanged
            print(
                f'{Fore.RED}Character "{char}": Not supported; '
                f'{Style.RESET_ALL}it will remain as it is.'
            )
            decrypted_text.append(char)

    print(
        f'-> 🔓 Decrypted Text: '
        f'[{Fore.YELLOW}{"".join(decrypted_text)}{Style.RESET_ALL}]'
    )


# Display the current encryption key
def show_key(encryption_key):
    print(f'- {Fore.GREEN}🔑 Current Key:{Style.RESET_ALL}')

    for char, key in encryption_key.items():
        if char == " ":
            char = "space"

        print(f"[{char} -> {key}]")


# Save the current key to a file
def key_save(key_save_name, keys):
    with open(key_save_name, "w") as file:
        file.write("".join(keys))

    print(f"{Fore.GREEN}🔑 The key has been saved!{Style.RESET_ALL}")


# Load and validate a key from a file
def load_key(key_name, chars):
    try:
        with open(key_name, "r") as file:
            keys_file = list(file.read())

            if keys_file:
                # Make sure the loaded key matches the original characters
                if (
                    len(keys_file) == len(chars)
                    and len(set(keys_file)) == len(chars)
                    and set(keys_file) == set(chars)
                ):
                    
                    loaded_keys = keys_file

                    encryption_key = dict(zip(chars, loaded_keys))
                    decryption_key = dict(zip(loaded_keys, chars))

                    print(f'{Fore.GREEN}✅ Key loaded successfully!{Style.RESET_ALL}')

                    return loaded_keys, encryption_key, decryption_key

                print(f"{Fore.RED}❌ Invalid key file!{Style.RESET_ALL}")
                return None

            print(f"{Fore.RED}❌ The file is empty!{Style.RESET_ALL}")
            return None

    except FileNotFoundError:
        print(f'- {Fore.RED}❌ File "{key_name}" does not exist!{Style.RESET_ALL}')
        return None


# Generate a new random encryption key
def generating_key(chars):
    print("🔄 Generating a new key...")

    keys = chars.copy()
    random.shuffle(keys)

    encryption_key = dict(zip(chars, keys))
    decryption_key = dict(zip(keys, chars))

    time.sleep(1)

    print(f'{Fore.GREEN}✅ New key generated successfully!{Style.RESET_ALL}')

    time.sleep(1.5)
    clear_screen()

    return keys, encryption_key, decryption_key


# Display the exit message
def exit_app():
    clear_screen()
    print("🚪 Thank you Hacker, Bye!")


# ------------------- # -- Main Program -- # ------------------- #

init()

divider = "#" + "-" * 50 + "#"

# Supported characters used by the encryption system
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Controls the main program loop
generating = True


# Main program loop
while generating:

    # Generate a key for the current session
    keys, encryption_key, decryption_key = generating_key(chars)

    while True:

        print(divider)
        print(f"-> {Fore.BLUE}🔐 Encryption Tool{Style.RESET_ALL} <-")
        print(divider)

        show_menu()

        print(divider)

        # Get the user's menu choice
        choice = input("📌 Choose an option: ").strip()

        print(divider)

        # Encrypt text
        if choice == "1":
            text = input("💬 Enter a text to encrypt: ")
            encrypt(text, chars, encryption_key)

        # Decrypt text
        elif choice == "2":
            text = input("💬 Enter a text to decrypt: ")
            decrypt(text, keys, decryption_key)

        # Show the current encryption key
        elif choice == "3":
            show_key(encryption_key)

        # Save the current key
        elif choice == "4":
            key_save_name = input("💾 Enter file name to save: ").strip()

            key_save(key_save_name, keys)

        # Load an existing key
        elif choice == "5":
            key_name = input("📂 Enter file name to load: ").strip()

            loaded_key = load_key(key_name, chars)

            if loaded_key is not None:
                keys, encryption_key, decryption_key = loaded_key

        # Generate a new key
        elif choice == "6":
            keys, encryption_key, decryption_key = generating_key(chars)

        # Exit the application
        elif choice == "7":
            exit_app()
            generating = False
            break

        # Handle invalid menu choices
        else:
            print(
                f"{Fore.RED}❌ Invalid input! "
                f"Please enter a number from 1 to 7."
                f"{Style.RESET_ALL}"
            )


# ------------------------------------------------------------ #