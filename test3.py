
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
    print("Public Key : ",public_key)
    print("Private Key : ",private_key)


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
    hashed = hashlib.sha1(message.encode("UTF-8")).hexdigest()
    print(hashed)
    return hashed

def verify(receivedHashed, message):
    ourHashed = hashFunction(message)
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
        
    for i in plaintext:
         pl=str(ord(i))
         M+=pl
    print("(M) Name in Series of numbers(ASCII) : ",M)
       
    #Dividing Text Into 3 Blocks ,So 
    z=re.findall('..',M)
    print("Number Divided into Blocks : ",z)
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
    print(Cipher)
    print(C)
    message=C
    hashFunction(message)
    print(len(Cipher))
    print(type(Cipher))    
# print("C after joining all Small Ciphers : ",C)

def decryption(Cipher,p,q):
    #c=int(CipherText)
    if len(CipherText) != 0 :
        

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
        print(M)

    else:
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
        print(M)
     


        
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
        Choice=int(input("Select a choice : \n 1. RSA Encryption \n 2. RSA Decryption \n 3.Diffie Hellman Key Exchange \n 4.Hashing \n Please Enter your Choice : "))
        
        #while Choice != 0 :
        if Choice == 1:
                plaintext =input("\n Please Enter the Text : ")
                Encryption(plaintext,p,q)
                decryption(Cipher,p,q)
        elif Choice ==2 :
                global CipherText
                CipherText=input
                decryption(CipherText,p,q)
        elif Choice ==3:
                key_exchange(p,q)
        elif Choice ==4 :
                text=input("")
                hashFunction(text)
        
















if __name__ == '__main__':
    main()