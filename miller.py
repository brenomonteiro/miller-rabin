import random
#10.  107 mod 29 = 17,
#a = 10 ** 7%29
#numerox = int("11100",2)
#int(0b11000000111001)
#print(bin(28)[2:])
#print(numero)
que=''
ka=0
numero = 5
numero1 = numero -1

numeroBinario =(bin(numero1)[2:])
palavra = str(numeroBinario)



for x in range(len(palavra)):
    if palavra[x] == '0':
        ka +=1
    if palavra[x] == '1':
        que = que + palavra[x]
        

a = random.randint(1,numero1)
b = a ** int(que,2)%numero
y = ka -1
print('boi',b)
if b == 1:
     print('inconclusive  tttt')
     
for x in range(y) :
    
   
    jj=2**x
    jjj = jj*int(que,2)
    c = a**jjj
    
    if c%numero == numero1:
         print('inconclusive')
    else:
        print('composite')
    
    '''
    print('oi',b)
    print('oik',ka-1)
    print('binario',ka)
    if b == -1:
         print('primo')
    else:
        b = b**2%numero 
print('composto')


print("ka",ka)
print("emi",int(emi,2))'''
    # TODO: write code…
#a**'''
