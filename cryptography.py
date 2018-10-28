"""
cryptography.py
Author: Claire
Credit: 

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associations=list(associations)


def encryption(x):
    enkey = input("Key: ")
    
    #turns input message to numbers
    x = list(x)
    a = 0
    b = []
    
    for m in x:
        (x.append(associations.index(m)))
    
    
    #turns key messsage to numbers
    c = []
    for m in enkey:
        (c.append(associations.index(m)))
    
    #adds numbers together
    d = []
    
    while a < len (b):
        d.append((b[a]+c[a%len(d)])%len(associations))
        x=x+1
    
    #turns numbers back to letters
    x = 0
    e = []
    
    while x<len(c):
        (e.append(associations[c[x]]))
        x=x+1
    
    
    #turns to a list 
    k = ""
    for m in e:
        k=k+m
    print (k)
    return (k)
    
    
def decryption(e):
    enkey = input("Key: ")
    
    #turns input message to numbers
    x = list(x)
    a = 0
    b = []
    #enkey = (str(input("Key: ")))
    #e = list(c)
    #c = []
    
    for m in x:
        (x.append(associations.index(m)))
    
    
    #turns key messsage to numbers
    c = []
    for m in enkey:
        c.append(associations.index(m))
    
    #adds numbers together
    d = []
    
    while a < len (b):
        d.append((b[a]+c[a%len(d)])%len(associations))
        x=x+1
    
    #turns numbers back to letters
    x = 0
    e = []
    
    while x<len(c):
        e.append(associations[c[x]])
        x=x+1
    
    
    #turns to a list 
    k = ""
    for m in e:
        k=k+m
    print (k)
    return (k)
    

def requesting_ans():
    req=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if req=="e":
        mess=str(input("Message: "))
        encryption(mess)
        requesting_ans()
    elif req=="d":
        mess=str(input("Message: "))
        decryption(mess)
        requesting_ans()
    elif req=="q":
        print("Goodbye!")
        return()
    else:
        print("Did not understand command, try again.")
        requesting_ans()
        
requesting_ans()
    
    
    
        