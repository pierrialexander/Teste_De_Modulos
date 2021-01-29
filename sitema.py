from Testes_de_modulos.lib.interface import *
from Testes_de_modulos.lib.arquivo import *
from time import sleep

arq = 'arquvio_de_teste.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m!')
    sleep(1)

