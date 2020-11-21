from fractions import gcd
import string
import numpy as npy


alp_freq = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.0236,0.0015,0.01974,0.00074]
alp_26=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
inp_cipher= input('Please enter your vigener cipher text:''\n').lower()
inp_cipher=list(inp_cipher)
lst_cipher=inp_cipher
a=0
b=[]
n=1

# Below code is the result of first n number of coincedents
while n<=30:
    
    # Below code is used to shift the list right
    lst_cipher = npy.roll(lst_cipher,1)
    
    # zip(x,y) is used in a such a way that it makes
    # [(x0,y0),(x1,y1)] for all the element of x and y
    for i,j in zip(inp_cipher,lst_cipher):
        
        # Below code compares and increments a if same element is found 
        if i==j:
            a+=1
    print('Number of coincidences for',n,'shift is:',a)
    b.append(a)
    n+=1
    a=0
    
# Below code is use to print number of coincidences
z1=max(b) # this is for highest number in the list
print('Maximum number of coincidence(z1):',z1)
z1=b.index(z1)
z1+=1

# Below code is for the second highest number in the list
z2=sorted(set(b))[-2]
print('Second highest number of coincidence(z2):',z2)
z2=b.index(z2)
z2+=1

# Below code is for the Third highest number in the list
z3=sorted(set(b))[-3]
print('Third highest number of coincidence:(z3)',z3)
z3=b.index(z3)
z3+=1

# Below code is for the fourth highest number in the list
z4=sorted(set(b))[-4]
print('Fourth highest number of coincidence:(z4)',z4)
z4=b.index(z4)
z4+=1

# Below code is for the fifth highest number in the list
z5=sorted(set(b))[-5]
print('Fifth highest number of coincidence(z5):',z5)
z5=b.index(z5)
z5+=1

# Below code is for the sixth highest number in the list
z6=sorted(set(b))[-6]
print('Sixth highest number of coincidence:(z6)',z6)
z6=b.index(z6)
z6+=1

values=[z1,z2,z3,z4,z5,z6]
print('\n'+'Possible key lengths are:''\n',z1,',',z2,',',z3,',',z4,',',z5,',',z6)
d1=gcd(z1,z2)
d1=gcd(d1,z3)
d1=gcd(d1,z4)
d1=gcd(d1,z5)
d1=gcd(d1,z6)
print('GCD of all above elements:',d1)

counter=0
while counter<=4:
    z1=values[counter]
    print('\n'+'If we take',z1,'as key length')

    # Below code is use to divide in z1 parts
    F=[[]for t1 in range(0,z1)]
    g1=0
    while g1<z1:
        for t2 in range(g1,len(inp_cipher),z1):
           F[g1].append(inp_cipher[t2])
        g1+=1
        
    # Below code is use to crack the cipher text
    g1=0
    Arr=[]
    while g1<z1:
        R=[]
        for st in alp_26:
            q = F[g1].count(st)
            q = q/26
            q = round(q,7)
            R.append(q)
        m =24
        N=[]
        e=0
        
        def lft_sft(l1,n1):
            # for left shift operation
            return l1[n1:] + l1[:n1]
            
        # Below code is for reverse mapping: numbers to letter
        rev_num = dict(zip(range(0,26),string.ascii_lowercase))

        while m>=0:
            L= lft_sft(alp_freq,e)
            A = npy.dot(R,L)
            A = round(A,6)
            N.append(A)
            m -= 1
            e+=1
        
        # for highest number in the list
        High1=max(N)
        
        # Below code is to retrieve the index of the maximum number
        E = [I for I, J in enumerate(N) if J==High1]
        E[0]=((26-E[0])%26)
        ind_key=rev_num[E[0]].upper()
        Arr.append(ind_key)
        D1=[]
        
        # Below loop is used for getting deciphered numbers
        for cha in F[g1]:
            dig = ord(cha) - 97
            dig = ((dig - E[0])%26)
            D1.append(dig)
        f2=[]
        
        # Below loop is used for mapping number to alphabet
        for id2 in D1:
            f2.append(rev_num[id2])
        F[g1]=f2
        g1+=1
    print('The Encryption Key:',''.join(Arr))    

    
    # Below code is use to fill the z1 parts into deciphered text 
    g1=0
    let=0
    Q1=[]
    v=int(len(inp_cipher)/z1)
    while let<v:
        while g1<z1:
            Q1.append(F[g1][let])
            g1+=1
        let+=1
        g1=0
    g1=0
    while g1<(len(inp_cipher)%z1):
        Q1.append(F[g1][let])
        g1+=1
    print('\n'+'Your plain Text:')
    print(''.join(str(elm) for elm in Q1))
    counter+=1
