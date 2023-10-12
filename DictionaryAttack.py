# This is a dictionary attack program

# Libraries
import hashlib

pass_found=0 # When the password is found the value changes

i_hash = input("Enter the hashed password: ")
p_doc = input("\nEnter password list filename including path: ") # gets file path from user

p_file = open(p_doc, "r") # opens doc in read only

for word in p_file:
    enc_word = word.encode('utf-8') # encodes hashed password to common format
    hash_word = hashlib.md5(enc_word.strip()) # convert value in enc_word and keep it in hash format
    digest = hash_word.hexdigest() # generate hash digest and store it

    if digest == i_hash:
        print("Password found: ", word)
        pass_found=1
        break

if not pass_found:
    print("Password not found")