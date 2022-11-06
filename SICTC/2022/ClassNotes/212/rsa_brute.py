#   a212_rsa_decrypt.py
import rsa as rsa

key = int(input("Enter the Decryption Key: " ))
#mod_value = int(input("Enter the Modulus: " ))
encrypted_msg = input("What message would you like to decrypt (No brackets): ")

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
mod_value=28400
data = open("./words.txt").readlines()
newdata = []
for i in data:
    i = i.replace("\n","")
    newdata.append(i)
del data

while True:
    mod_value+=1
    print(mod_value)
    try:#28459
        nmsg = rsa.decrypt(key,mod_value, msg)
        print(nmsg)
    except:
        ()
    for i in msg:
        if i in newdata:
            print(msg)
