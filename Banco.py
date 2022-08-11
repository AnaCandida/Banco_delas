import string
import secrets
import time

class Cliente:
    def __init__(self,nome,mulher, renda):
        self._nome = nome 
        self._mulher = mulher
        self._renda = float(renda) 
        # self._senha = senha
 
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
        self._cheque_especial = 0
    
    @property
    def conta(self):
        return self._conta

    @property
    def titulares(self):
        nomes = []
        for cliente in self._titulares:
            nomes.append(cliente.nome)
        return (',').join(nomes)


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
    
    @cheque_especial.setter
    def cheque_especial(self, valor):
        self._cheque_especial = valor




    def permissao_cheque(self):
        qtd_mulheres = 0
        total_renda = 0
        for cliente in self._titulares:
            if cliente.mulher == True:
                qtd_mulheres += 1
                total_renda += float(cliente.renda)
                media_renda = total_renda/qtd_mulheres
                self.cheque_especial = media_renda
                return True
            else:
                self.cheque_especial_ = 0
                return False            
        
    def sacar(self,valor):
        permissao = self.permissao_cheque()
        if self.saldo > 0 and self.saldo >=valor:
            print(f'Iniciando operação para sacar {valor}')
            self.saldo -= valor
            print(f'Operação realizada. Saldo:{self.saldo}')
            print('-------------------------------------------------------------------------------------------')
        elif permissao:
            limite = self.cheque_especial
            # from pdb import set_trace;set_trace()

            if (self.saldo - valor) >= (-limite):
                self.saldo -= valor
                print('Cheque especial ativado!')
                print(f'Operação realizada. Saldo:{self.saldo} Limite: {self.cheque_especial} Disponível:{limite + self.saldo}')
                print('-------------------------------------------------------------------------------------------')
            else:
                print('Limite do cheque especial atingido!')
                print(f'Operação não realizada. Saldo:{self.saldo} Limite: {limite} Disponível:{limite + self.saldo}')
                print('-------------------------------------------------------------------------------------------')
        else:
            print('***Saldo insuficiente. Sem permissão de cheque especial***')
            print(f'Operação não realizada. Saldo: {self.saldo}')

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
        print('\n****************************')
        print('BEM VINDA AO BANCO DELAS!')
        print('****************************')
        print('O que deseja?\n')
        print("1 - Abrir conta")
        print("2 - Ver Saldo")
        print("3 - Adicionar Titular")
        print("4 - Sacar")
        print("5 - Depositar")
        print("6 - Sair\n")

        escolha = input('Digite a opção desejada: ').upper()

        match escolha:
            case "1":
                print('-------------------------------------------------------------------------------------------')
                print("Oba!! Vamos abrir uma conta!")
                print('-------------------------------------------------------------------------------------------')

                Banco_delas.abrir_conta()

            case "2":
                print('-------------------------------------------------------------------------------------------')
                print("Beleza! Vamos verificar seu saldo!")
                print('-------------------------------------------------------------------------------------------')

                titular = input('Digite seu nome:')
                senha = (input('Digite sua senha:')).upper()
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                conta = conta_valida.get('conta')
                print(f'Número da conta: {conta.conta} Saldo: {conta.saldo} Titular(s):{conta.titulares}')
                time.sleep(3)
                Banco_delas.voltar_menu()
               
            case "3":
                print('-------------------------------------------------------------------------------------------')
                print("Opa! Vamos adicionar mais um titular!")
                print("Mas primeiro, vamos validar seu acesso a conta!")
                print('-------------------------------------------------------------------------------------------')

                titular = input('Digite seu nome:')
                senha = (input('Digite sua senha:')).upper()
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                conta = conta_valida.get('conta')
                Banco_delas.add_titular(conta)
                print(f'Operação realizada. Titular(s):{conta.titulares}')   
                time.sleep(3)
                Banco_delas.voltar_menu()         
      
            case "4":
                print('-------------------------------------------------------------------------------------------')
                print("Vamos sacar!")
                print('-------------------------------------------------------------------------------------------')

                titular = input('Digite seu nome:') 
                senha = (input('Digite sua senha:')).upper()
                valor = float(input('Qual o valor? '))
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                conta = conta_valida.get('conta')
                conta.sacar(valor=valor)
                time.sleep(3)
                Banco_delas.voltar_menu()
            
            case "5":
                print('-------------------------------------------------------------------------------------------')
                print("Vamos depositar!\n")
                titular = input('Digite seu nome:')
                senha = (input('Digite sua senha:')).upper()
                valor = float(input('Qual o valor? '))
 
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                conta = conta_valida.get('conta')
                conta.depositar(valor=valor)
                time.sleep(3)
                Banco_delas.voltar_menu()
            
            case "6":
                print('\n-------------------------------------------------------------------------------------------')
                print("Até logo!")
                print("Obrigada por escolher o Banco Delas!\n")
          
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
                print("Até logo! ")
                print("Obrigada por escolher o Banco Delas!")

    def validar_titular(titular, senha):
        for i, conta in enumerate(Banco_delas.contas):
            # from pdb import set_trace;set_trace()
            if senha == conta.get('senha'):
                    print(f'achei {conta}')
                    conta_valida = conta
                    return conta_valida
            elif titular == conta.get('titular'):
                    print('Oops! Senha inválida')
                    time.sleep(3)
                    Banco_delas.abrir()
            else:
                print(f'\nConta não localizada. Titular informado: {titular}')
                time.sleep(3)
                Banco_delas.abrir()
        else:
            print(f'\nConta não localizada. Titular informado: {titular}')
            time.sleep(3)
            Banco_delas.abrir()
    
    def add_titular(self,conta:Conta_corrente):
        nome= input('Digite o nome do novo titular: ')
        mulher = input('Novo titular se declara mulher? 1-Sim 2-Não 3-Prefiro não responder! ')
        match mulher:
            case "1":
                mulher = True
            case _:
                mulher = False
        renda = float(input('Digite a renda mensal do novo titular:'))
        cliente = Cliente(nome=nome,mulher=mulher, renda=renda)
        conta._titulares.append(cliente)

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
        cliente = Cliente(nome=nome,mulher=mulher, renda=renda)
       
        numero += 1
        dados_conta = Conta_corrente(cliente=cliente, numero = numero, senha = senha)
        Banco_delas.contas.append({
                'titular': cliente.nome,
                 'numero': numero,
                 'senha': senha.upper(),
                 'conta': dados_conta
            })
        print('-------------------------------------------------------------------------------------------')
        print('Conta criada com sucesso! Bem vinda ao nosso Banco!')
        print(f'Salve sua senha de acesso gerada automaticamente:{senha}')
        time.sleep(3)
        Banco_delas.voltar_menu()

    def __str__(self):
        total_clientes = len(Banco_delas.contas) 
        return f'Numero de clientes: {total_clientes}'

Banco_delas.abrir()
print(Banco_delas())