import string
import secrets
import time
import statistics

class Cliente:
    def __init__(self,nome,mulher, renda,senha):
        self._nome = nome 
        self._mulher = mulher
        self._renda = float(renda) 
        self._senha = senha
 
    @property
    def nome(self):
        return self._nome
    
    @property
    def mulher(self):
        return self._mulher
        
    @property
    def renda(self):
        return self._renda

    @property
    def senha(self): 
        return self._senha

    def __str__(self):
        return (f'Cliente :{ self.nome} , mulher: {self.mulher} renda: {self.renda}, senha:{self.senha}')


class Conta_corrente():
    def __init__(self, cliente:Cliente, numero,senha):
        self._conta = numero
        self._titulares = [cliente]
        self._senha = senha
        self._saldo = 0        
        self._cheque_especial = Conta_corrente.verificar_cheque_especial(self)
    
    @property
    def conta(self):
        return self._conta

    @property
    def titulares(self):
        return self._titulares

    @property
    def senha(self):
        return self._senha

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        self._saldo = valor

    @property
    def cheque_especial(self):
        return self._cheque_especial

  
    def verificar_cheque_especial(self):
        cheque_especial = []
        for cliente in self.titulares:
            # from pdb import set_trace;set_trace()
            if Cliente.mulher is True:
                cheque_especial.append(cliente.renda)
                valor = statistics.mean(cheque_especial)
            else:
                valor = 0        
                
        return valor
        
    def sacar(self,valor,nome):

        titular_acessando =  Conta_corrente.validar_titular(self,nome)
        
        if titular_acessando :
            print(f'Iniciando operação saque{valor}')
            if self.titular[titular_acessando].mulher == True:
                print(self.saldo)
                if self.saldo >= 0 and self.saldo < self.cheque_especial :

                    self.saldo -= valor 
                    print(f'Operação realizada. Saldo:{self.saldo}')
                else:
                    print(f'Valor excede limite. Saldo:{self.saldo}')

            elif(self.saldo > 0):
                self.saldo -= valor
                print(f'Operação realizada. Saldo:{self.saldo}')
            else:
                print(f'Valor excede limite. Saldo:{self.saldo}')
        else:
            raise Exception('Cliente informado não é titular dessa conta.')

    def depositar(self,valor):
        self.saldo += valor
        print(f'Iniciando operação para depositar {valor}')

        print(f'Operação realizada. Saldo:{self.saldo}')
        print('-------------------------------------------------------------------------------------------')

    def __str__(self):
        return f'{self.conta} {self.titulares}{self._senha}{self.saldo} {self.cheque_especial}'


class Banco_delas():
    contas = []
    

    def __init__(self):
       pass

    def abrir():
        Banco_delas()
        print('****************************')
        print('BEM VINDA ao BANCO DELAS!')
        print('****************************')
        print('O que deseja?')
        print("1 - Abrir conta")
        print("2 - Ver Saldo")
        print("4 - Adicionar Titular")
        print("5 - Sacar")
        print("6 - Depositar")
        print("7 - Sair")

        escolha = input('Digite a opção desejada:').upper()

        match escolha:
            case "1":
                print('-------------------------------------------------------------------------------------------')
                print("Ebaaa!! Vamos abrir uma conta!\n")
                Banco_delas.abrir_conta()

            case "2":
                print('-------------------------------------------------------------------------------------------')

                print("Insira seu nome:ver dados")
                titular = input('Digite seu nome:')
                senha = (input('Digite sua senha:')).upper()
                # valor = float(input('Qual o valor? '))
 
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                tentativas = 0
                if True in conta_valida:
                    # from pdb import set_trace;set_trace()
                    conta = conta_valida[1].get('conta')
                    # permissão = 'não'
                    # if conta.get('mulher') == True:
                    #     permissão = 'sim'
                    #     valor_cheque_especial = conta.get('cheque_especial')

                    print(f'Conta: {conta.conta} Saldo: {conta.saldo}')
                    # \n Cheque_especial:{permissão} -- {valor_cheque_especial}')
                 
                    time.sleep(3)
                    Banco_delas.voltar_menu()
                elif tentativas <= 3:
                    print('Senha inválida')
                    tentativas += 1
                    time.sleep(3)
                    Banco_delas.abrir()
                else:
                    print('****************************')
                    print('Você atingiu o limite de tentativas inválidas.')
                    time.sleep(3)
                    Banco_delas.voltar_menu()
                

            case "3":
                print('-------------------------------------------------------------------------------------------')

                print("Insira seu nome:cadastro")
            
            case "4":
                print('-------------------------------------------------------------------------------------------')

                print("Insira seu nome:novo titular")

            case "5":
                print('-------------------------------------------------------------------------------------------')

                print("Insira seu nome:sacar")
            case "6":
                print('-------------------------------------------------------------------------------------------')
                print("Vamos depositar!\n")
                titular = input('Digite seu nome:')
                senha = (input('Digite sua senha:')).upper()
                valor = float(input('Qual o valor? '))
 
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                tentativas = 0
                if True in conta_valida:
                    conta = conta_valida[1].get('conta')
                    conta.depositar(valor)
                    time.sleep(3)
                    Banco_delas.voltar_menu()
                elif tentativas <= 3:
                    print('Senha inválida')
                    tentativas += 1
                    time.sleep(3)
                    Banco_delas.abrir()
                else:
                    print('****************************')
                    print('Você atingiu o limite de tentativas inválidas.')
                    time.sleep(3)
                    Banco_delas.voltar_menu()

            case "7":
                print('-------------------------------------------------------------------------------------------')
                print("tchau")
                print("Obrigada por escolher o Banco Delas!")

            case "P":
                from pdb import set_trace;set_trace()

            case _:
                print('-------------------------------------------------------------------------------------------')
                print(f'Você digitou {escolha}.Esta opção não esta no menu!\nEscolha entre os números de 1-7.\nCaso precise de ajuda, acesse: www.bancodela.com ou entre em contato com a sua agência')
                print('-------------------------------------------------------------------------------------------')
                time.sleep(7)
                Banco_delas.abrir()

    def voltar_menu():
        print('****************************')
        print("1 - Voltar ao menu principal")
        print("2 - Sair")
        escolha1 = input('O que dejesa agora?')

        match escolha1:
            case '1':
                Banco_delas.abrir()
            case _:
                print('-------------------------------------------------------------------------------------------')
                print("tchau")
                print("Obrigada por escolher o Banco Delas!")

    def validar_titular(titular, senha):
        for i, conta in enumerate(Banco_delas.contas):
            if senha == conta.get('senha'):
                    print(f'achei {conta}')
                    conta_valida = conta
                    return (True, conta_valida)

    def abrir_conta():
        numero = 0
        nome= input('Digite seu nome completo: ')
        mulher = input('Você se declara mulher? 1-Sim  2-Não 3-Prefiro não responder! ')
        match mulher:
                case "1":
                    mulher = True
                case "2":
                    mulher = False
                case _:
                    mulher = False
        renda = float(input('Digite sua renda mensal:'))

        # try:
        alphabet = string.ascii_letters + string.digits
        senha  = ''.join(secrets.choice(alphabet) for i in range(8))
        Cliente(nome=nome,mulher=mulher, renda=renda, senha = senha)
       
        numero += 1
        dados_conta = Conta_corrente(Cliente, numero = numero, senha = senha)
        Banco_delas.contas.append({
                'titular': Cliente.nome,
                 'numero': numero,
                 'senha': senha.upper(),
                 'conta': dados_conta
            })
        print('-------------------------------------------------------------------------------------------')
        print('Conta criada com sucesso! Bem vinda ao nosso Banco!')
        print(f'Salve sua senha de acesso gerada automaticamente:{senha}')
        time.sleep(3)
        Banco_delas.voltar_menu()

   

    def add_titular(self,cliente:Cliente):
        pass

    def __str__(self):
        total_clientes = len(Banco_delas.contas) 
        return f'Numero de clientes: {total_clientes}'

Banco_delas.abrir()

# Banco_delas.abrir_conta()
# print(Banco_delas.contas[0]['conta'])a


# CqxZS5z1