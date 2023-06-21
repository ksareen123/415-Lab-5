#Used and edited by Krish Sareen

# This is udpserver.py file
import socket                       
import math

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

def polyalpha_enc(plaintxt,key):
    ciphertext = ""
    print("using key " + key)
    textsize = len(plaintxt)
    keysize = len(key)
    for i in range (textsize):
        encryptedchar = ord(plaintxt[i]) + ord(key[i % keysize])
        #print("Adding " + plaintxt[i] + " (" + str(ord(plaintxt[i])) + ") " + key[i % keysize] + " (" + str(ord(key[i % keysize])) + ") " + " = " + str(encryptedchar % 128)) 
        encryptedchar = encryptedchar % 128
        ciphertext += (chr(encryptedchar))

    return ciphertext
    
def polyalpha_dec(ciphertxt,key):
    plaintxt = ""
    print("using key " + key)
    textsize = len(ciphertxt)
    keysize = len(key)
    for i in range (textsize):
        encryptedchar = ord(ciphertxt[i]) - ord(key[i % keysize])
        #print("Subtracting " + str(i) + " index: " + ciphertxt[i] + " (" + str(ord(ciphertxt[i])) + ") " + key[i % keysize] + " (" + str(ord(key[i % keysize])) + ") " + " = " + str(encryptedchar % 128)) 
        encryptedchar = encryptedchar % 128
        plaintxt += (chr(encryptedchar))
    return str(plaintxt)

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
        dec_let = (( ord(letter) ** d) % n)
        decryptedtext = decryptedtext + chr(dec_let)
        dec_list.append(dec_let)

    print(dec_list)
    print(decryptedtext)

    return decryptedtext

# create a UDP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Get local machine address
ip = "10.229.143.64"                          

# Set port number for this server
port = 13000                                          

# Bind to the port
serversocket.bind((ip, port))           

#compute_Keys_RSA()
e = int(input("enter e value: "))
d = int(input("enter d value: "))
n = int(input("enver n value: "))
print("Waiting to receive message on port " + str(port) + '\n')

polykey_encrypted = ""
# Receive the data of 1024 bytes maximum. Need to use recvfrom because there is not connecction
data, addr = serversocket.recvfrom(1024)
print("received polyalphabetic cipherkey: " + data.decode())
polykey_encrypted = data.decode()

polykey = RSA_decrypt(polykey_encrypted, d, n)

#send acknowledgement
ack = "Connection established."
sent = serversocket.sendto(ack.encode(), addr)
print("sent acknowledgement")

while True:  

   # Receive the data of 1024 bytes maximum. Need to use recvfrom because there is not connecction
   data, addr = serversocket.recvfrom(1024)
   print("received encrypted: " + data.decode())

   msg = data.decode()
   print("decrypted: " + polyalpha_dec(msg, polykey))

   print("Type your reply below")
   reply = input("->")  

   encryptedreply = polyalpha_enc(reply, polykey)
   
   if (reply == "bye"):
      print("")
      print("Waiting to receive message on port " + str(port) + '\n')
      sent = serversocket.sendto(reply.encode(), addr)

   else:
      print('sent ' + encryptedreply)
      sent = serversocket.sendto(encryptedreply.encode(), addr)

   

