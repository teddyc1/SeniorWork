# TODO: I have an issue with pycryptodome not installing correctly. I was messing with my environment
#   trying to get python 2.7 to work for fastcol and I ended up messing up my real work environment.
#   Most of this is pseudocode to prove I have some idea of what I'm supposed to do for a padding oracle attack
#   and maybe earn a point or two.
# Crypto is cool!!
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


# Key used for everything, global variable
key = 'Crypto is cool!!'


def checkpadding(ciphertext):
    # The function CheckPadding() will take as input a ciphertext, decrypt it with
    # the hardcoded key and return true or false indicating whether padding is correct
    # or not (this is your padding oracle)
    dec = decrypt(cipertext, key)
    checkPadding(dec)
        # verify that the last bits match correctly. x x x x x x x 01, x x x x x x 02 02 and so on
        if padding == correct return True
    return False


def paddingoracle(Ciphertext):
    # The function Padding Oracle() will take as input a file that includes a cipherext
    # (encrypted under AES-CBC using the hardcoded key). The size ciphertext will
    # have to be a multiple of 16 bytes, else you can terminate.
    # Your function should now perform the padding oracle attack using the
    # CheckPadding() method described above in order to decrypt the given
    # ciphertext.
    # You will have to keep counter on how many times you had to call the the
    # CheckPadding() function.
    # Your code should return the decryption (i.e. plaintext) and the counter (i.e.
    # how many times you called the CheckPadding() function).
    if size(len) % 16 != 0
        terminate
    counter = 0
    for i in range(0,256)
        > find padding
        if(checkpadding(ciphertext)):
            found padding time to xor
        counter += 1
    time to xor
    then repeat until decryption is done
    return (decryption,counter)

def main():
    file = open("Ciphertext", "r")
    print(file.read())
    paddingoracle(file)


if __name__ == '__main__':
    main()