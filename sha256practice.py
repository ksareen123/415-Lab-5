from hashlib import sha256 

#open and read csv input file
inputfile = open("lab_test_data.csv", "rb")
data = inputfile.read()
inputfile.close()

print(data)
#encode string, actually not necessary as the default is bytes
encoded_input = data

#use hash algorithm
inputhash = sha256(encoded_input)
hex_hash = inputhash.hexdigest()

#print
print("hash value: " + hex_hash)

#password hashing
#mypassword = input("Enter your password: ")
#print("Password: " + mypassword)
#encodedpwd = mypassword.encode()
#print("Encoded bits: " + str(encodedpwd))
#hsh = sha256(encodedpwd)
#hex_digits = hsh.hexdigest()
#print("hash value: " + hex_digits)


