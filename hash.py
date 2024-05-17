import hashlib
import sys
import pyfiglet
import os

ascii_banner = pyfiglet.figlet_format("HASH CRACKER")
print(ascii_banner)

print("Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA 224 | SHA384")

hash_type = str(input("What's the hash type? "))
wordlist_location = str(input("Enter wordlist location: "))
hash = str(input("Enter hash: "))

# Use 'with' statement to open the file and automatically close it after use
with open(wordlist_location, 'r') as word_list_file:
    word_list = word_list_file.read()
    
lists = word_list.splitlines()

for word in lists:
    if hash_type == "MD5":
        hash_object = hashlib.md5(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word}\n")
    elif hash_type == "SHA1":
        hash_object = hashlib.sha1(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word}\n")
    elif hash_type == "SHA224":
        hash_object = hashlib.sha224(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word}\n")
    elif hash_type == "SHA512":
        hash_object = hashlib.sha512(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word}\n")
    elif hash_type == "SHA224":
        hash_object = hashlib.sha224(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word}\n")
    elif hash_type == "SHA384":
        hash_object = hashlib.sha384(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[1;32m HASH FOUND: {word}\n")
    else:
        print("Please choose from the given options.")