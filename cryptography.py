"""
cryptography.py
Author: Claire
Credit: none

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associations=list(associations)


def encryption(t):
    enkey=input("Key: ")
    
    #turns input message to numbers
    t=list(t)
    h=0
    wa=[]
    for i in t:
        (wa.append(associations.index(i)))
    
    
    #turns key messsage to numbers
    m=[]
    for i in enkey:
        (m.append((associations.index(i))))
    
    #adds numbers together
    l=[]
    while h<len(wa):
        (l.append((wa[h]+m[h%len(m)])%len(associations)))
        h=h+1
        
        
    #turns numbers back to letters
    h=0
    d=[]
    while h<len(l):
        (d.append(associations[l[h]]))
        h=h+1
    
    

    #turns to a list 
    a=""
    for i in d:
        a=a+i
    print(a)
    return(a)


def decryption(d):
    enkey=str(input("Key: "))
    d=list(d)
    l=[]
    for i in d:
        (l.append(associations.index(i)))
    m=[]
    for i in enkey:
        (m.append(associations.index(i)))
    
    h=0
    wa=[]
    while h<len(l):
        (wa.append(((l[h]-m[h%len(m)])%len(associations))))
        h=h+1
    h=0
    t=[]
    while h<len(wa):
        (t.append(associations[wa[h]]))
        h=h+1
    a=""
    for i in t:
        a=a+i
    print(a)
    return(a)
    
    
    
def requesting_ans():
    put=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if put=="e":
        text=str(input("Message: "))
        encryption(text)
        requesting_ans()
    elif put=="d":
        text=str(input("Message: "))
        decryption(text)
        requesting_ans()
    elif put=="q":
        print("Goodbye!")
        return()
    else:
        print("Did not understand command, try again.")
        requesting_ans()
        
requesting_ans()