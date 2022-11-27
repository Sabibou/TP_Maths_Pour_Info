def code_inverse(message) :
	trad=[]
	for lettre in message:
		trad.insert(0,lettre)
	return ''.join(trad)

def pgcd(a,b):
	if a>b:
		for i in range(2,b+1):
			if a%i==0 and b%i==0:
				return i
	else:
		for i in range(2,a+1):
			if a%i==0 and b%i==0:
				return i
	return 1


def euclide_etendu(a,n):
	i=2
	r=[a,n]
	u=[1,0]
	v=[0,1]
	q=[0,r[0]//r[1]]
	flag=True
	while(flag):
		r.append(r[i-2]%r[i-1])
		if(r[i]==0):
			break
		q.append(r[i-1]//r[i])
		u.append(u[i-2]-q[i-1]*u[i-1])
		v.append(v[i-2]-q[i-1]*v[i-1])

		i+=1

	
	return u[i-1]

def cesar(mot, alphabet, n, b, mode):

	mot2=list(mot)
	alphabet2=list(alphabet)
	trad=[]

	if b>=n or b<0:
			b=b%n

	if mode =='c':
		print("Voici le mot à crypter : ",mot)
		for i in range(len(mot2)):
			try:
				index=alphabet2.index(mot2[i],0,n)			
			except:
				index=0
			index=(index+b)%n
			trad.append(alphabet2[index])

	if mode =='d':
		print("Voici le mot à décrypter : ",mot)
		for i in range(len(mot2)):
			try:
				index=alphabet2.index(mot2[i],0,n)   #si le caractere nest pas dans lalphabet on met par defaut le premier carac
			except:
				index=0
			index=index=(index-b)%n
			trad.append(alphabet2[index])


	return ''.join(trad)


def cesar_aff(mot, alphabet, n, a, b, mode):
	while pgcd(a,n)!=1:
		a=int(input("Rentrez un a valide\n"))

	if b>=n or b<0:
			b=b%n

	mot2=list(mot)
	alphabet2=list(alphabet)
	trad=[]


	if mode =='c':
		print("Voici le mot à crypter : ",mot)
		for i in range(len(mot2)):
			try:
				index=alphabet2.index(mot2[i],0,n)
			except:
				index=0
			index=((a*index)+b)%n
			trad.append(alphabet2[index])

	if mode =='d':
		print("Voici le mot à décrypter : ",mot)
		a1=euclide_etendu(a,n) #a', l'inverse multiplicatif de a
		b1=((-a1)*b)%n
		for i in range(len(mot2)):
			try:
				index=alphabet2.index(mot2[i],0,n)
			except:
				index=0
			index=((a1*index)+b1)%n
			trad.append(alphabet2[index])

	return ''.join(trad)

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz,.?éếù"
Alphabet2= """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_
'abcdefghijklmnopqrstuvwxyz£"""
mot=cesar("Chez moi, le secret est enfermé dans une maison aux solides cadenas dont la clé est perdue et la porte scellée.", Alphabet, len(Alphabet), 1000, "c")
print(cesar(mot, Alphabet, len(Alphabet), 1000, "d"))
mot2=cesar_aff("BONJOUR",Alphabet,len(Alphabet),3,3,'c')
print(cesar_aff(mot2,Alphabet,len(Alphabet),3,3,'d'))