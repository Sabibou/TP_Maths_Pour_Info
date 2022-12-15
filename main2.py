import random

def pgcd(a,b):
    if b==0:
        return a
    else:
        return pgcd(b,a%b)

premiers=[2,3,5,7,11,13,17,19,23]

def phi(p,q):
	return (p-1)*(q-1)

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

def temoin_miller(n, a):
    s=0
    n2=n-1
    while n2%2==0 and n2!=0:
        s+=1
        n2//=2
    d=(n-1)/pow(2,s)  #soit s et d de la sorte que n-1=2^s*d
    x=pow(a,d)%n
    if x==1 or x ==n-1:
        return False
    for i in range(s-1):
        x=pow(x,2)%n
        if x==n-1:
            return False
    return True #n est composé car a est un témoin de miller

def miller_rabin(n,k):  #n un entier impair >=3 et k un entier >=1(nombre de boucle)
    for i in range(k):
        a = random.randint(2, n-1)
        if temoin_miller(n,a)==True:
            return False
    return True   #n est probablement premier


def chiffrage(M,E,N):
	if M>N:
		print("probleme")
	else:
		return pow(M,E)%N

def dechiffrage(C,D,N):
	return pow(C,D)%N

def verifE(E,p):
	return E<p and pgcd(E,p)==1



print("Exercice 1\n")
N, E, D, C = 391, 151, 7, 17
print("1- Le message déchiffré par Alice est : M' = ", dechiffrage(C,D,N))
print("2- Nombres premiers p et q et déduction de \u03C6(N) ")
p,q = 23,17
print('p = {} et q = {}'.format(p,q))
print('On déduit \u03C6(N) = {} * {} = {}'.format(p-1,q-1,phi(p,q)))
print("3- D est l'inverse multiplicatif de E modulo \u03C6(N) et D = {}".format(euclideE(E,phi(p,q))))

print("\nEercice 2\n")
N, E, D, M = 221, 11, 35, 112
print("1-a Le message chiffré est C = {}".format(chiffrage(M,E,N)))
C = 78
print("1-b Le message déchiffré est M' = {}".format(dechiffrage(C,D,N)))
p, q = 53, 71
print("2-a N = {}*{} et \u03C6(N) = {}".format(p,q,phi(p,q)))
E = 307
print("2-b E acceptable?",verifE(E,phi(p,q)), "; et D =",euclideE(E,phi(p,q)))

print("\nExercice 3\n")

R = 1
while R == 1: #pour arrêter le programme
    a = int(input("Valeur de M ou C : "))
    b = int(input("Valeur de E ou D : "))
    N = int(input("Valeur de N : "))
    R = pow(a,b)%N
    print(R)
    R = input("Voulez vous faire une autre opération?(o/n)")
    if R == 'o':
        R = 1
    else:
        R = 0


