#Caesar Cipher

#Encryption - right shift
def encryp(s):
    encryp=""
    for i in s:
        if(i.islower()):
            encryp=encryp+chr((ord(i)+3 -97)%26 +97)
        else:
            encryp=encryp+chr((ord(i)+3 -65)%26 +65)       
        
    return encryp

#Decryption - right shift
def decryp(s):
    decryp=""
    for i in s:
        if(i.islower()):
            decryp=decryp+chr((ord(i)-3-97)%26 +97)
        else:
            decryp=decryp+chr((ord(i)-3-65)%26 +65)
    return decryp

print("1.Encryption")
print("2.Decryption")
ch=int(input("Enter your choice:"))
if (ch==1):
    S=input("Enter the data:")    
    encrypted=encryp(S)
    print("The encrypted data is",encrypted)
elif (ch==2):
    S=input("Enter the data:")
    decrypted=decryp(S)
    print("The decrypted data is",decrypted)
else:
    print("Incorret choice")

