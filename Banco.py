import os
import time

def menu():
    
    os.system('cls || clear') 
    saldo = 100.0
    deposito = 0.0
    saque = float
    ultimo_deposito  = float
    
    print('==========Menu==========')
    print('S-Saque \nD-Depósito \nE-Consultar Extrato \nF-Fechar')
    
    opc = str (input('Selecione Uma Das Opções Acima!'))
    
    select(opc,saldo,deposito,saque,ultimo_deposito)
    
    
    

def select(opc,saldo,deposito,saque,ultimo_deposito):
    if opc == "S":
        
        os.system('cls || clear')
        print('Saque Selecionado:')
        
        print(f'Seu Saldo É De R${saldo}')
        
        saque = float (input('Quanto Deseja Sacar?'))
        
        time.sleep(2)
        
        
    elif opc == "D":
        os.system('cls || clear')
        print('Depósito Selecionado:')
        deposito = float (input('Insira A Quantia Do Depósito:'))
        
        saldo = saldo + deposito
        
        print(f'Saldo Atual {saldo}')
        time.sleep(2)
        
        
        
    elif opc == "E":
        os.system('cls || clear')
        
        print('Extrato Selecionado:')
        print(f'Saldo Em Conta R${saldo}.')
        
        ultimo_deposito = ultimo_deposito =+ deposito
        
        print(f'Último Depósito R${ultimo_deposito}.')
        time.sleep(2)
        
    elif opc == "F":
        os.system('cls || clear')
        print('Fechando.')
        time.sleep(2)
        
      


        
        
        
        
while True:        
    
    menu()
    
    

