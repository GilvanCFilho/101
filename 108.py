"""
"not" é usado para inverter expressões ;
not true = false 
not false = true
"""
senha =input('Senha :')

if senha == '123456' :
    print('Entrou')

elif not senha:
    print('campo vazio') #ex : not em input 

else:
    print('senha incorreta')

