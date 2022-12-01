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

def chiffrage(M,N,E):
	if M<N:
		print("probleme")
	else:
		return pow(M,E)%N

def dechiffrage(C,D,N):
	return pow(C,D)%N

def verifE(E,p):
	return E<p and pgcd(E,p)==1



print("EX 1\n")
print(pow(17,7)%391)
print(phi(23,17))
print("D=",euclideE(151,352))

print("\nEX 2\n")
print("C=", chiffrage(112,11,221))
print("M'=",dechiffrage(78,35,221))
print("N=",53*71," p(N)=",phi(53,71))
print("E acceptable?",verifE(307,3640), " D=",euclideE(307,3640))

print("\nEX 3\n")
print(pow(1001,353)%1073)
print(54%26)


