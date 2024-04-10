"""
vars : usadas para salvar dados na memoria 

"""

var_dois = int ('2') #ex var int

cod = 'A'
bar = 100
hype_bar = bar >= 77

print('cod:', cod, 'bar:', bar)
print('Is it hyperbar?', hype_bar)

"""
Agora , exemplos operações aritimeticas abaixo
"""

adição = 10 + 10 
print('adição',adição)
subtração = 10 - 10
print('subtração', subtração)
multiplicação = 10 * 10
print('multiplicação', multiplicação)
divisão = 10 / 2.2 #sempre float
print('divisão', divisão)
divisão_inteira = 10 // 2.2 # sempre float
print('divisão inteira', divisão_inteira)
exponenciação = 2 ** 10 
print('exponenciação',exponenciação)
resto = 10 % 2 
print('resto', resto)
 

print(71 % 2 == 0)

A = 10
B = 2
print(A % B == 0 )


"""
calc in var 
"""
calc_102 = 36 + 235 / 3 *10 **2
print(calc_102)

"""
f-strings usadas para ativar vars dentro de strings
"""

a_b = 195
b_c = 142

soma = a_b + b_c

sla_1 = f'a soma de {a_b} e {b_c} é igual {soma}'

print(sla_1) #ex de fstring
