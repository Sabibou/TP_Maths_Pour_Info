
message = input("Entrer votre message :")
def crypt(mess):
    traduction = ""
    i = len(mess) - 1
    while(i>-1):
        traduction = traduction + mess[i]
        i -=1
    return traduction

m = message
#print(m)
#print(crypt(m))

## Code César Simple
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cesar(message):
    b = int(input("Nombre de décalages :"))
    mode = input("Crypatge ('c') ou décryptage('d') :")
    if mode == 'd':
        b = -b%len(alphabet)
    messchi = []
    messdchi =[]
    messd =""

    for i in message:
        if i in alphabet:
            k = alphabet.find(i)
            messchi.append(k)

    for j in messchi:
        j = (j+ b)%len(alphabet)
        messdchi.append(j)
    for i in messdchi:
        messd += alphabet[i]
    return messd


#print(cesar(m))

##Code César affine
def pgcd(a,b):
    if b==0:
        return a
    else:
        return pgcd(b,a%b)

def euclideE(a,b):
    r=[a,b]
    q=[0]
    v=[0,1]
    u=[1,0]
    #r.append(a)
    #r.append(b)
    
    i = 2
    while r[i-1]!=0:
        r.append(r[i-2] % r[i-1])
        q.append(r[i-2] // r[i-1])
        u.append(u[i-2] - q[i-1] * u[i-1])
        v.append(v[i-2] - q[i-1] * v[i-1])
        i+=1
        
    return u[i-2]

#print(euclideE(15,9))




#print(pgcd(3,6))

def acesar(message):
    a = int(input("Valeur de a :"))
    if pgcd(a,len(alphabet))!=1:
        print("a n'est pas premier avec la taille de l'alphabet")
        a = int(input("Valeur de a :"))
    b = int(input("Valeur de b :"))
    mode = input("Crypatge ('c') ou décryptage('d') :")
    if mode == 'd':
        a = euclideE(a,len(alphabet))
        b = (-a*b)%len(alphabet)
    messchi = []
    messdchi =[]
    messd =""

    for i in message:
        if i in alphabet:
            k = alphabet.find(i)
            messchi.append(k)

    for j in messchi:
        j = (a*j + b)%len(alphabet)
        messdchi.append(j)
    for i in messdchi:
        messd += alphabet[i]
    return messd


print(acesar(m))
