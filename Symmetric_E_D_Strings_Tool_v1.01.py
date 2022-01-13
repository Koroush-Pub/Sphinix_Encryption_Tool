"""
simple symmetric encryption and decryption tool
created by Koroush Arian
"""

import platform
import subprocess
from cryptography.fernet import Fernet
import os

def input_for_decryption():
    key = input("\nPlease Enter Your Decryption Key:(STRING INPUT)\n").encode()
    message = input("\nPlease Enter Your Encrypted Message:(STRING INPUT)\n").encode()
    return message,key #return thease as binary strings

def input_for_encryption():
    key = input("\nPlease Enter Your Encryption Key:(STRING INPUT)\n").encode()
    message = input("\nPlease Enter Your Message:(STRING INPUT)\n").encode()
    return message,key

def make_new_key():
    key = Fernet.generate_key()  # store in a secure location
    print(f"\nThis Is Your New (Encryption&Decryption) Key:\n\n{key.decode()}\n\nkeep it safe!\n")

def encrypt(message:bytes, key:bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

def welcoming():
    path = os.path.dirname(__file__) + "\\banner.txt"
    with open(path,"r") as wl:
        print(''.join([line for line in wl]))


def clear_screen():
    # Clear command as function of OS
    command = "cls" if platform.system().lower()=="windows" else "clear"

    # Action
    subprocess.call(command,shell=True)

if __name__ == "__main__":
    clear_screen()
    welcoming()
    while True:
        try:
            choise = int(input("Choose One Of The Numbers U Want:\n\n1)Just Make A New Key\n2)Encrypt Message\n3)Decrypt Message\n4)Exit\n>>"))

            if choise == 1:
                make_new_key()

            elif choise == 2:
                try:
                    message,key = input_for_encryption()
                    #encrypt(message,key)
                    print(f"your encrypted message is:\n{encrypt(message,key).decode()}")
                except:
                    print("\nEncryption Error Try Again\n")
            elif choise == 3:
                try:
                    message,key = input_for_decryption()
                    #decrypt(message,key)
                    print(f"Decryption is successfull!\nur decrypted message is:\n{decrypt(message,key).decode()}")
                except:
                    print("\nDecryption Error Try Again\n")

            elif choise == 4:
                print("EXITING")
                clear_screen()
                break

            else:
                pass

        except:
            print("\nInputError!\n(Maybe U Enter SomeThing Wrong,Try again.)\n")
