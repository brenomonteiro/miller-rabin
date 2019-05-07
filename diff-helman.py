
 

PrimoCompartilhado = 23    
baseCompartilhada = 5      
 
a = 6    
b = 15      
 

 
# Alice Manda A 
A = (baseCompartilhada**a) % PrimoCompartilhado
print( 'Alice manda A: ' , A )
 
# Bob manda B 
B = (baseCompartilhada ** b) % PrimoCompartilhado 
print( 'Bob manda B: ', B )

# Alice 
aliceChaveSecreta = (B ** a) % PrimoCompartilhado
print( 'Alice chave secreta: ', aliceChaveSecreta)
 
# Bob 
bobchaveSecreta = (A**b) % PrimoCompartilhado
print( 'Bob chave secreta: ', bobchaveSecreta)
