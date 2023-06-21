import math
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def compute_Keys_RSA():
    p = int(input("choose the first prime number: "))
    q = int(input("choose the second prime number: "))
    n = p * q
    print("n = " + str(n))
    totient = math.lcm((p - 1), (q - 1))
    print("Totient(n) = " + str(totient))
    """
    for i in range(2,totient):
        if (math.gcd(i,n) == 1):
            if (is_prime(i)):
               print(i)
    """
    e = int(input("Choose one of these numbers: "))
    #e * d = 1 mod(totient)
    #d = (1 / e) % totient
    d = pow(e,-1,totient)
    print("d = " + str(d))
    print("Kpub, share = (" + str(e) + ", " + str(n) + ")")
    print("Kpriv, do NOT share = (" + str(d) + ", " + str(n) + ")")
compute_Keys_RSA()

def RSA_encrypt(message, e, n):
    #𝑐𝑖 =  𝐸𝑃𝑈𝐵(𝑚𝑖)  =  (𝑚𝑒𝑖 ) 𝑚𝑜𝑑𝑢𝑙𝑢𝑠 𝑛
    #encrypting to send to me
    ciphertext = []

    print("encrypting using public key")

    for letter in message :
        num_letter = ord(letter)
        encryptedletter = (num_letter ** e) % n 
        ciphertext.append(encryptedletter)

    print(ciphertext)
    return ciphertext

def RSA_decrypt(ciphertext, d, n):
    #𝐷𝑃𝑅𝐼𝑉(𝑐𝑖)  =  (𝑐𝑑𝑖 ) 𝑚𝑜𝑑𝑢𝑙𝑢𝑠 𝑛

    #decrypting to read for me
    decryptedtext = ""
    dec_list = []
    print("decrypting using private key")

    for letter in ciphertext:
        dec_let = (letter ** d) % n
        decryptedtext = decryptedtext + chr(dec_let)
        dec_list.append(dec_let)

    print(dec_list)
    print(decryptedtext)

    return decryptedtext

message = input("enter message: ")

e = int(input("enter e: "))
n = int(input("enter n: "))

cipher = RSA_encrypt(message, e, n)

d = int(input("Enter d: "))

m_dec = RSA_decrypt(cipher, d, n)

p = 47
q = 71
n = p * q
totient_n = (p - 1) * (q - 1)

e = 97
d = 1693

