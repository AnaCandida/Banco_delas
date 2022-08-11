from abc import ABC, abstractmethod
import string # senha
import secrets #senha
import time #painel

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

    # @property
    # def senha(self): 
    #     return self._senha

    def __str__(self):
        return (f'Cliente :{ self.nome} , mulher: {self.mulher} renda: {self.renda}, ')

class Conta(ABC):
    def __init__(self, cliente:Cliente, senha):
        self._titular_principal = cliente
        self._senha = senha
        self._saldo = 0   

    @property
    def conta(self):
        return self._conta
    
    @property
    def titular_principal(self):
        return self._titular_principal 
    
    @property
    def senha(self):
        return self._senha
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        self._saldo = valor

    def depositar(self,valor):
        self.saldo += valor
        print(f'Iniciando operação para depositar {valor}')

        print(f'Operação realizada. Saldo:{self.saldo}')
        print('-------------------------------------------------------------------------------------------')

    @abstractmethod
    def sacar(self, valor):
        pass


class Conta_corrente(Conta):
    def __init__(self, numero,titular,senha):
        super().__init__(titular,senha)
        self._conta = numero
        self._cheque_especial = 0
        self._titulares = [titular]
    
    @property
    def titulares(self):
        nomes = []
        for cliente in self._titulares:
            nomes.append(cliente.nome)
        return (',').join(nomes)

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

   

    def __str__(self):
        permissao = self.permissao_cheque()
        return f'Conta de número{self.conta} - Titulares:{self.titulares} -Senha: {self._senha} -Saldo: {self.saldo} - Cheque_especial{permissao}' 
class Banco_delas():
    contas = []
    tempo_painel = 2
    

    def __init__(self):
        self.numero_contas = len(Banco_delas.contas)

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

        escolha = input('Digite a opção desejada: ')

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
                senha = (input('Digite sua senha:'))
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                if conta_valida:
                    conta = conta_valida.get('conta')
                    permissao = conta.permissao_cheque()
                    message_saldo = f'Número da conta: {conta.conta} Saldo: {conta.saldo} Titular(s):{conta.titulares}'
                    if permissao:
                        message_cheque_especial = f' | Direito a cheque especial. Limite: {conta.cheque_especial} |'
                    print (message_saldo + message_cheque_especial) if permissao else message_saldo
                    
                    time.sleep(Banco_delas.tempo_painel)
                    Banco_delas.voltar_menu()
               
            case "3":
                print('-------------------------------------------------------------------------------------------')
                print("Opa! Vamos adicionar mais um titular!")
                print("Mas primeiro, vamos validar seu acesso a conta!")
                print('-------------------------------------------------------------------------------------------')

                titular = input('Digite seu nome:')
                senha = (input('Digite sua senha:'))
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                if conta_valida:
                    conta = conta_valida.get('conta')
                    Banco_delas.add_titular(conta=conta)
                    print(f'Operação realizada. Titular(s):{conta.titulares}')   
                    time.sleep(Banco_delas.tempo_painel)
                    Banco_delas.voltar_menu()         
      
            case "4":
                print('-------------------------------------------------------------------------------------------')
                print("Vamos sacar!")
                print('-------------------------------------------------------------------------------------------')

                titular = input('Digite seu nome:') 
                senha = (input('Digite sua senha:'))
                valor = float(input('Qual o valor? '))
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                if conta_valida:
                    conta = conta_valida.get('conta')
                    conta.sacar(valor=valor)
                    time.sleep(Banco_delas.tempo_painel)
                    Banco_delas.voltar_menu()
            
            case "5":
                print('-------------------------------------------------------------------------------------------')
                print("Vamos depositar!\n")
                titular = input('Digite seu nome:')
                senha = (input('Digite sua senha:'))
                valor = float(input('Qual o valor? '))
                conta_valida =  Banco_delas.validar_titular(titular=titular, senha=senha)
                if conta_valida:
                    conta = conta_valida.get('conta')
                    conta.depositar(valor=valor)
                    time.sleep(Banco_delas.tempo_painel)
                    Banco_delas.voltar_menu()
            
            case "6":
                print('\n-------------------------------------------------------------------------------------------')
                print("Até logo!")
                print("Obrigada por escolher o Banco Delas!\n")
          
            case _:
                print('-------------------------------------------------------------------------------------------')
                print(f'Você digitou {escolha}.Esta opção não esta no menu!\nEscolha entre os números de 1-7.\nCaso precise de ajuda, acesse: www.bancodela.com ou entre em contato com a sua agência')
                print('-------------------------------------------------------------------------------------------')
                time.sleep(Banco_delas.tempo_painel)
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

        conta_valida = False
        for i, conta in enumerate(Banco_delas.contas):
            if titular in conta.get('conta').titulares:
                if senha == conta.get('senha'):
                        # print(f'achei {conta}')
                        conta_valida = conta
                else:
                    print('Oops! Senha inválida')
                    time.sleep(Banco_delas.tempo_painel)
                    Banco_delas.abrir()
        
        if conta_valida:
            return conta_valida
        else:
            print(f'\nConta não localizada. Titular informado: {titular}')
            time.sleep(Banco_delas.tempo_painel)
            Banco_delas.abrir()
      
    
    def add_titular(conta:Conta_corrente):
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
       
        numero = (Banco_delas().numero_contas) + 1
        
        dados_conta = Conta_corrente(titular=cliente, numero=numero, senha=senha)
        Banco_delas.contas.append({
                'titular_principal': cliente.nome,
                 'numero': numero,
                 'senha': senha,
                 'conta': dados_conta
            })
        print('-------------------------------------------------------------------------------------------')
        print('Conta criada com sucesso! Bem vinda ao nosso Banco!')
        print(f'Salve sua senha de acesso gerada automaticamente:{senha}')
        time.sleep(Banco_delas.tempo_painel)
        Banco_delas.voltar_menu()

    def __str__(self):
        for conta in Banco_delas.contas:
            print('-------------------------------------------------------------------------------------------')
            print(f'Conta = {conta}\n')
            dados = conta.get('conta')
            print(f'Dados = {dados}')

        return f'\nNumero de clientes: {Banco_delas().numero_contas}'

Banco_delas.abrir()
print(Banco_delas())
# from pdb import set_trace;set_trace()

