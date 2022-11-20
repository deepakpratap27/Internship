
import hashlib
import math

import re









def rsa(p,q):
    global e,n,d
    check__prime(p)
    check__prime(q)
    n=p*q
    et=(p-1)*(q-1)
    #l=[]
    for i in range(2,et-1):
        if math.gcd(et,i)==1:
            #l.append(e)
           e=i
           break
    #e=l[0]
    d=mod_Inv(e,et)
    public_key=(e,n)
    private_key=(d,n)
    print("\n Public Key : ",public_key)
    print("\n Private Key : ",private_key)


def mod_Inv(x,y):
        for i in range(y):
            if (x*i)%y==1:
                return i
 
def check__prime(self):
        for i in range(2,self//2):
            if (self%i)==0:
                print(self,"is not a prime number ,Enter a prime number")
            break


def gc(a,b):
    while b != 0:
        a, b = b, a % b
    return a


def primRoots(q):
 roots = []
 required_set = set(a for a in range (1,q) if gc(a,q) == 1)
 for g in range(1,q):
    actual_set = set(pow(g,i) %q for i in range (1, q))
    if required_set == actual_set:
        roots.append(g)
 return roots



def hashFunction(message):
    global hashed
    hashed = hashlib.sha1(message.encode("UTF-8")).hexdigest()
    print("\nThe Hash Value of Cipher : ",hashed)
    return hashed

def verify(receivedHashed, Hash_Cipher):
    ourHashed = Hash_Cipher
    if receivedHashed == ourHashed:
        print("Verification successful: ", )
        print(receivedHashed, " = ", ourHashed)
    else:
        print("Verification failed")
        print(receivedHashed, " != ", ourHashed)
 





def key_exchange(p,q):
         #Diffie-Helman Key Exchange
         check__prime(p)
         check__prime(q)
         primitive_roots = primRoots(p)
         print("Primitive Roots : ",primitive_roots)
         al=int(input("Please Select a Primitive Root : "))
         #Exchange of private Keys of two persons Ex: Scar anf Jox
         Xs=int(input("Enter the Private Key of Scar : "))
         Xj=int(input("Enter the Private key of Jox : "))
         Ys=int()
         print("Public Key of Scar : " )
         Yj=int("Public Key of Jox  : ")

         if Xs<p:
            Ys=pow(al,Xs,p)
         if Xj < p :
            Yj=pow(al,Xj,p)

         JoxSecret=pow(Ys,Xj,p)
         ScarSecret=pow(Yj,Xs,p)
         if JoxSecret == ScarSecret:
            print("The Secret Key  for communication =",JoxSecret,ScarSecret)

def Encryption(plaintext,p,q):
    global Cipher

    plaintext=plaintext.upper()
    pl=""
    M=""
    #if len(plaintext)%2==0:
    print("\n \n \n Encryption Starts \n \n \n")
    for i in plaintext:
         pl=str(ord(i))
         M+=pl
    print("\n (M) Name in Series of numbers(ASCII) : ",M)
       
    #Dividing Text Into 3 Blocks ,So 
    z=re.findall('..',M)
    print(" \n Number Divided into Blocks : \n",z )
    le=int((len(M))/2)
    C=''
    rsa(p,q)
    Cipher=[]
    for i in range(le):
        s=z[i]
        m=int(s)
        if m<n:
            c=(pow(m,e,n))
            c=str(c)
            Cipher.append(c)
            C+=c
    print("\nThe Cipher text : ",Cipher)
    print("\nCipher : ",C)
    Hash_Cipher=C
    print(type(Hash_Cipher))
    hashFunction(Hash_Cipher)
    print("\n Length of the Cipher \n",len(Cipher))
    print("\n \n \n Encryption Ends \n \n \n")    
# print("C after joining all Small Ciphers : ",C)

def decryption(Cipher,p,q):
    #c=int(CipherText)
    h=""
    for i in range(len(Cipher)):
        s=Cipher[i]
        s=str(s)
        h+=s
    hashFunction(h)
    verify(h,Hash_Cipher)
    rsa(p,q)
    l=[]
    for i in range(len(Cipher)):
        Cip=Cipher[i]
        Cip=int(Cip)
        m=(pow(Cip,d,n))
        l.append(m)
    M=""
    for i in l:
        M+=chr(i)
    M=str(M).lower()
    print("After Decrypting the PlainText : ",M)
     


        
#for i in CipherText:
 #z=re.findall('......',CipherText)
 #le=int((len(CipherText))/6)
    #M=""
 #for i in range(le):
 #s=z[i]
 #f=int(s)
   
   # rsa(p,q)
    #m=(pow(c,d,n))
   # m=str(m)
   
   # M+=m
    #print("C After Splitting into Small Ciphers : ",z)
    #print("M : ",M) 
    
    #v=re.findall('..',m)
    #le=int((len(m))/2)
    #M=""
    
    
    #for i in range(le):
        #s=v[i]
        #m=int(s)
        #pl=(chr(m))
        #M+=pl
    #print("Plaintext : ",M)
























def main():
        p=int(input("Enter a Prime Number : "))
        q=int(input("Enter a Prime Number : "))
        Choice=int(input("Select a choice : \n 1. RSA Encryption \n 2. RSA Decryption \n 3. Diffie Hellman Key Exchange \n 4. Hashing \n Please Enter your Choice : "))
        
        #while Choice != 0 :
        if Choice == 1:
                plaintext =input("\n Please Enter the Text : ")
                Encryption(plaintext,p,q)
                decryption(Cipher,p,q)
        elif Choice ==2 :
                CipherText=input("")
                decryption(CipherText,p,q)
        elif Choice ==3:
                key_exchange(p,q)
        elif Choice ==4 :
                text=input("")
                hashFunction(text)
        
















if __name__ == '__main__':
    main()