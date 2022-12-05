


##Code Inverse

def crypt(mess):
    traduction = "" #on créé un mot vide qui va contenir le message inversé
    i = len(mess) - 1 #on affecte à i la taille du message moins 1
    while(i>-1): #i>-1 pour prendre en compte le cas où i=0
        traduction = traduction + mess[i]
        i -=1 #on décrémente de 1 
    return traduction

##Alphabets

Alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Alphabet2 = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{é}£ """


## Code César Simple

def cesar(message,alphabet):
    print("Cryptage/Décryptage avec César Simple")
    b = int(input("Clé de chiffrement :")) # b représente la clé de chiffrement
    mode = input("Cryptage ('c') ou décryptage('d') :")
    if mode == 'd':
        b = -b%len(alphabet) # recalcul de b pour le déchiffrement
    messchi = [] # création d'une liste vide qui va contenir le message chiffré(indices dans l'alphabet choisi)
    messdchi =[] # création d'une liste vide qui va contenir le message dechiffré(indices dans l'alphabet choisi)
    traduction ="" # création d'un mot vide qui va contenir la traduction du message déchiffré

    for i in message: # parcours de chaque lettre du message
        if i in alphabet:
            k = alphabet.find(i)# si la lettre se trouve dans l'alphabet choisi, on récupère et on affecte la valeur de l'indice correspondant dans k
        else :
            k=0 #si la lettre n'est pas dans l'alphabet, on met par défaut la première lettre de l'alphabet
        messchi.append(k) # actualisation de la liste du message chiffré

    for j in messchi: # parcours des chiffres dans le message chiffré
        j = (j+ b)%len(alphabet) # mise à jour de la valeur des chiffres(indices) en utilisant  y=(x-b)mod n avec n la taille de l'alphabet choisi
        messdchi.append(j) # actualisation de la liste du message déchiffré
    for i in messdchi:
        traduction += alphabet[i] # transformation des chiffres en lettres
    return traduction


##Code César affine
#Fonction pgcd

def pgcd(a,b):
    if b==0: # test d'arrêt
        return a
    else:
        return pgcd(b,a%b)

#Fonction Euclide Etendu
def euclideEtendu(a,b):
    r=[a,b] # initialisation de la liste des restes contenant la clé a et la taille de l'alphabet choisi
    q=[-1]  # initialisation de la liste des quotients (-1 pour signifier que la division par 0 est impossible avec des entiers)
    u=[1,0] # initialisation de u0 et u1 
    v=[0,1] # initialisation de v0 et v1 
    
    i = 2 # initialisation de i à 2
    while r[i-1]!=0: # test d'arrêt (lorsque le reste est nul)
        r.append(r[i-2] % r[i-1]) # mise à jour de la liste des restes
        q.append(r[i-2] // r[i-1])
        u.append(u[i-2] - q[i-1] * u[i-1])
        v.append(v[i-2] - q[i-1] * v[i-1])
        i+=1 # incrémentation de 1
        
    return u[i-2] # retour de l'avant dernière valeur de u qui va correspondre à l'inverse multiplicatif de la clé de chiffrement a


def cesarAffine(message,alphabet): 
    print("Cryptage/Décryptage avec César Affine")
    a = int(input("Valeur de a :")) # clé de chiffrement a
    while pgcd(a,len(alphabet))!=1: # vérification que la clé a et la taille de l'alphabet sont premiers entre eux
        print("a n'est pas premier avec la taille de l'alphabet")
        a = int(input("Valeur de a :"))
    b = int(input("Valeur de b :")) # clé de chiffrement b
    mode = input("Cryptage ('c') ou décryptage('d') :")
    if mode == 'd':
        a = euclideEtendu(a,len(alphabet)) # calcul de l'inverse multiplicatif pour obtenir la clé de déchiffrement a'
        b = (-a*b)%len(alphabet) # calcul de b'
    messchi = [] #création d'une liste vide qui va contenir le message chiffré(indices dans l'alphabet choisi)
    messdchi =[] #création d'une liste vide qui va contenir le message dechiffré(indices dans l'alphabet choisi)
    traduction ="" #création d'un mot vide qui va contenir la traduction du message déchiffré

    for i in message:
        if i in alphabet: # parcours de chaque lettre du message
            k = alphabet.find(i) # affectation de la valeur de l'indice correspondant à i dans k, si i se trouve dans l'alphabet choisi, on récupère et on affecte la valeur de l'indice correspondant dans k
        else :
            k=0 #si la lettre n'est pas dans l'alphabet, on met par défaut la première lettre de l'alphabet
        messchi.append(k) # actualisation de la liste du message chiffré

    for j in messchi: # parcours des chiffres dans le message chiffré
        j = (a*j + b)%len(alphabet) # mise à jour de la valeur des chiffres(indices) en utilisant  y=(a'x+b')mod n avec n la taille de l'alphabet choisi
        messdchi.append(j) # actualisation de la liste du message déchiffré
    for i in messdchi:
        traduction += alphabet[i] # transformation des chiffres en lettres
    return traduction





##Programme principal
print("#########################################################################")
print("#################PROGRAMME DE CRYPTAGE/DECRYPTAGE########################")
print("#########################################################################")

#alphabet = input("""Quel alphabet voulez vous-utilisez (1 ou 2)? \n 1- Alphabet1 =ABCDEFGHIJKLMNOPQRSTUVWXYZ \n 2- Alphabet2 =!"#$%&'\()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyzéèë}{£" \n Réponse :""")
#myTemplate = "{} = {}"
#statement = myTemplate.format("alphabet", alphabet)
#exec(statement)

num_alph=int(input("""Quel alphabet voulez vous-utilisez (1 ou 2)? \n 1- Alphabet1 =ABCDEFGHIJKLMNOPQRSTUVWXYZ \n 2- Alphabet2 =!"#$%&'\()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyzéèë}{£" \n Réponse :"""))
if num_alph==1:
    alphabet=Alphabet1
else:
    alphabet=Alphabet2

## Jeux d'essais
m1 = "Si deux hommes ont la même opinion. L’un d’eux est de trop"
m2 = """ 'snoçel sed ennod em no uq sruojuot sap emia n ej euq neib erdnerppa a terp sruojuot sius ej' """
m3 = "Cyhfibhffnhermertneqreybvaqnafyrcnffrcyhfibhfireermybvaqnafyrshghee"
m4 = """ ""Chez moi, le secret est enfermé dans une maison aux solides cadenas dont la clé est perdue et la porte scellée."-Les milles et une nuits" """

num_message = int(input("Quel message voulez-vous utilisez ? \n Pour votre propre message saissisez un chiffre supérieur à 4 :"))
if num_message == 1:
    m = m1
elif num_message == 2:
    m = m2
elif num_message == 3:
    m = m3
elif num_message == 4:
    m = m4
else:
    m = input("Entrer votre message :")

code = int(input("Choississez le type de code à utiliser :\n 1-Code inverse\n 2-Code César\n 3-Code César affine\n"))
if code ==1 :
    print(crypt(m))
elif code ==2:
    print(cesar(m,alphabet))
else :
    print(cesarAffine(m,alphabet))