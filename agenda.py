def adicionar(nome, telefone, email):
    contatos[nome] = {'Telefone': telefone, 'E-mail': email, 'Favorito': False}
    print('\nContato adicionado!')
    return

def ver_contatos(contatos):
    if contatos:
        for chave, valor in contatos.items():
            status = '★' if valor['Favorito'] else ''
            print(f'[ {status} ] Nome: {chave.upper()}\n'
              f'Número: {valor['Telefone']}\n'
              f'E-mail: {valor['E-mail']}\n')
    else:
        print('\nLista vazia.')
    return
    

def editar_contato(contatos, nome, opcao, novo):
    if opcao == '1':
        contatos[novo] = contatos.pop(nome)
    elif opcao == '2':
        contatos[nome]['Telefone'] = novo
    elif opcao == '3':
        contatos[nome]['E-mail'] = novo
    print(f'\nContato atualizado!')
    return

def favoritar(contatos, nome):
    if nome in contatos:
        contatos[nome]['Favorito'] = True
        print(f'\n{nome} foi adicionado como favorito.') 
    else:
        print(f'\nO contato {nome} não existe.')
    return

def deletar(contatos, nome):
    if nome in contatos:
        contatos.pop(nome)
        print('\nContato removido.')

    else:
        print('\nContato não encontrado.')

    return

def desmarcar_favorito(contatos, nome):
    if nome in contatos:
        if contatos[nome]['Favorito']:
            contatos[nome]['Favorito'] = False
            print('\nContato desfavoritado.')
        else:
            print(f'\nO contato {nome.capitalize()} não está marcado como favorito.')
    else:
        print('\nContato inexistente.')


def ver_favoritos(contatos):
    for chave, valor in contatos.items():
        if valor['Favorito']:
            print((f' ★ Nome: {chave.upper()}\n'
              f'Número: {valor['Telefone']}\n'
              f'E-mail: {valor['E-mail']}\n')) 
        else:
            print('\nAinda não há contatos favoritos!')
    return


contatos = {}
while True:
    menu = ('\nOPÇÕES: \n'
        '|1| = ADICIONAR CONTATO\n'
        '|2| = VER CONTATOS\n'
        '|3| = EDITAR CONTATO\n'
        '|4| = MARCAR / DESMARCAR FAVORITO\n'
        '|5| = DELETAR CONTATO\n'
        '|6| = VER FAVORITOS\n'
        '|7| = SAIR\n')
    
    print(menu)

    escolha = input('Escolha uma das opções acima: ')

    if escolha == '1':
        nome = input('Nome do contato: ')
        numero = input('Número: ')
        email = input('E-mail: ')
        adicionar(nome, numero, email)

    elif escolha == '2':
        print('\nCONTATOS\n')
        ver_contatos(contatos)

    elif escolha == '3':

        if nome in contatos:

            nome = input('Informe o nome do contato que deseja editar: ')
            print(f'Nome: {nome.upper()}\n'
              f'Telefone: {contatos[nome]['Telefone']}\n'
              f'E-mail: {contatos[nome]['E-mail']}\n'
              )

            opcao = input('\nOPÇÕES\n'
                      '|1| - Nome\n'
                      '|2| - Número\n'
                      '|3| - E-mail\n'
                       'Selecione a opção que quer alterar: ')
            
            novo = input('Digite a alteração: ')
            
            editar_contato(contatos, nome, opcao, novo )
            
        else:
            print('\nContato não encontrado.')
        
    elif escolha == '4':
        opcao = input('|1| - MARCAR CONTATO COMO FAVORITO\n'
                      '|2| - DESMARCAR FAVORITO\n'
                       'Escolha o número referente a opção desejada: ')
        if opcao == '1':
            nome = input('Digite o nome do contato para favoritar: ')
            favoritar(contatos, nome)
        elif opcao == '2':
            nome = input('Digite o nome do contato para desfavoritar: ')
            desmarcar_favorito(contatos, nome)
        else:
            print('Opção inválida.')

    elif escolha == '5':
        nome = input('Digite o nome do contato a ser deletado: ')
        deletar(contatos, nome)

    elif escolha == '6':
        ver_favoritos(contatos)

    elif escolha == '7':
        print('FIM')
        break

    else:
        print('Escolha uma opção válida.')