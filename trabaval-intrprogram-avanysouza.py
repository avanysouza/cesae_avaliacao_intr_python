import random
import time

def validarPin(pin_utilizador):
    """
    Esta função valida o pin inserido pelo utilizador, comparando com a variável global pin_utilizador.
    Argumentos: pin_utilizador (string)
    Retorno: se o pin estiver correto retorna valor booleano True para exibir o menu de opções. Se for inválido, será apresentada mensagem de erro.
    """
    tentativas = 0
    while tentativas < 3:
        pin = input("Informe a senha de acesso da conta: ")
        if pin == pin_utilizador:
            print("Bem vindo ao Banco Cesae!")
            return True
        else:
            tentativas += 1
            print(f"PIN de acesso incorreto. Tentativas restantes: {3 - tentativas}")

    print("Número de tentativas excedido. Cartão apreendido")

def exibirMenu():
    """
    Exibe o menu e apresenta as opções para o utilizador escolher.

    Retorno: realiza a leitura da opção digitada pelo utilizador e guarda o valor.
    """
    print("\nMenu:")
    print("1 - Realizar levantamentos")
    print("2 - Consultar saldo")
    print("3 - Realizar depósitos")
    print("4 - Pagamentos")
    print("5 - Sorteio do dia")
    print("6 - Sair")
    return input("Informe o número da operação desejada: ")


def levantamentos(saldo):
    """
    Realiza a operação de levantamento de dinheiro da conta conforme o saldo disponivel no momento.
    Será realizada uma validação para que o valor informado não seja superior a 400 euros, igual/inferior a 0
    ou inferior ao saldo atual disponivel na conta.

    Argumentos: saldo(float) - o saldo atual da conta

    Retorno: saldo atualizado com decréscimo do valor informado pelo utilizador após validação.
    """
    valor = eval(input("Informe o valor a levantar: "))
    if valor <= 0:
        print("Valor inválido para levantamento. Insira valor superior a 0€")
        time.sleep(2)
    elif valor > 400:
        print("Não pode levantar mais de 400€ por dia.")
        time.sleep(2)
    elif valor > saldo:
        print("Saldo insuficiente.")
        time.sleep(2)
    else:
        saldo -= valor
        print(f"Levantamento realizado com sucesso! Saldo: {saldo:.2f}€.")
        time.sleep(2)
    return saldo


def exibirSaldo(saldo):
    """
    Exibe o saldo atual da conta.

    Argumentos: saldo(float) - o saldo atual da conta

    """
    print(f"Saldo atual: {saldo:.2f}€")
    time.sleep(2)


def depositos(saldo):
    """
    Realiza a operação de depósito conforme valor informado pelo utilizador.
    Será realizada uma validação para que o valor informado não seja superior a 2500 euros ou igual/inferior a 0.
    Argumentos: saldo(float) - o saldo atual da conta
    Retorno: saldo atualizado com acréscimo do valor informado pelo utilizador.
    """
    valor = eval(input("Informe o valor a depositar: "))
    if valor <= 0:
        print("Valor inválido para depósito.")
        time.sleep(2)
    elif valor > 2500:
        print("Não é possível depositar mais de 2500€ por dia.")
        time.sleep(2)
    else:
        saldo += valor
        print(f"Depósito realizado com sucesso. Novo saldo: {saldo:.2f}€")
        time.sleep(2)
    return saldo


def pagamentos(saldo):
    """
    Realiza a operação de pagamento conforme a entidade, referência e o valor informado pelo utilizador.
    Será realizada uma validação para que o valor informado não seja superior ao saldo atual da conta ou igual/inferior a 0.
    Argumentos: saldo(float) - o saldo atual da conta
    Retorno: saldo atualizado com decréscimo conforme valor informado pelo utilizador.

    """
    entidade = input("Informe a entidade: ")
    referencia = input("Informe a referência: ")
    valor = eval(input("Informe o valor a pagar: "))
    if valor <= 0:
        print("Valor inválido para pagamento.")
        time.sleep(2)
    elif valor > saldo:
        print("Saldo insuficiente.")
        time.sleep(2)
    else:
        saldo -= valor
        print(f"Pagamento realizado com sucesso! Saldo: {saldo:.2f}€")
        time.sleep(2)
    return saldo


def sorteio(saldo, sorteioRealizado):
    """
    Realiza a operação de sorteio com geração de número aleatório através da função randint.
    Será realizada uma validação booleana (True ou False) para verificar se o utilizador já realizou a operação no dia.

    Argumentos: saldo(float) - o saldo atual da conta e sorteioRealizado - booleano para validar numero de sorteios realizados.

    Retorno: se o utilizador acertar o número aleatório, o valor será somado ao saldo atual da conta, retornando um saldo atualizado.
    A variável booleana sorteioRealizado mudará seu valor para True.
    """
    if sorteioRealizado:
        print("Você já tentou jogar hoje!Volte amanhã!")
        return saldo, sorteioRealizado

    aposta = int(input("Adivinhe o número entre 1 e 100: "))
    numeroSorteado = random.randint(1, 100)
    print("Número da sorte:", numeroSorteado)
    if aposta == numeroSorteado:
        saldo += numeroSorteado
        print(
            f"Parabéns, hoje é seu dia de sorte! Você acertou e {numeroSorteado}€ foram adicionados ao seu saldo. Saldo disponível: {saldo:.2f}€.")
    else:
        print("Que pena, hoje não foi seu dia de sorte.")
    time.sleep(2)
    return saldo, True


#VARIÁVEIS
saldo = 0.0
pin_utilizador = "cesae123"
sorteioRealizado = False


if validarPin(pin_utilizador):
    while True:
        opcao = exibirMenu()
        match opcao:
            case "1":
                saldo = levantamentos(saldo)
            case "2":
                exibirSaldo(saldo)
            case "3":
                saldo = depositos(saldo)
            case "4":
                saldo = pagamentos(saldo)
            case "5":
                saldo, sorteioRealizado = sorteio(saldo, sorteioRealizado)
            case "6":
                print("Até logo! Obrigada por utilizar o Banco Cesae.")
                break


