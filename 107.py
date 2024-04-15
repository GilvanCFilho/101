entrada = input(' [E]ntrada [S]aida ')
senha_digitada = input('Senha:')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')

if entrada == 'E':
    print('Entrar')
else:
    print('Sair')