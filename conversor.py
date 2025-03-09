def conversor_moeda(valor, de, para):
    # Taxas de câmbio fictícias com BRL como referência
    taxas = {
        "BRL": 1.0,   # 1 BRL = 1.0 BRL
        "USD": 5.79,  # 1 USD = 5.79 BRL
        "EUR": 5.61,  # 1 EUR = 5.61 BRL
    }

    # Verificar se as moedas são válidas
    if de not in taxas or para not in taxas:
        return "Moeda inválida!"

    # Se as moedas de origem e destino forem iguais, não há conversão
    if de == para:
        return valor

    # Converter o valor de qualquer moeda para BRL primeiro, depois para a moeda de destino
    if de == "BRL":
        # Se a moeda de origem é BRL, converte dividindo pela taxa da moeda de destino
        valor_convertido = valor / taxas[para]
    elif para == "BRL":
        # Se a moeda de destino é BRL, converte multiplicando pela taxa da moeda de origem
        valor_convertido = valor * taxas[de]
    else:
        # Para conversões entre moedas diferentes de BRL, converte para BRL e depois para a moeda de destino
        valor_convertido = (valor * taxas[de]) / taxas[para]

    return valor_convertido

# Função para garantir que o valor inserido é um número válido
def solicitar_valor():
    while True:
        try:
            valor = float(input("Digite o valor a ser convertido: "))
            if valor <= 0:
                print("Por favor, insira um valor positivo.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

# Função para garantir que a moeda inserida seja válida
def solicitar_moeda(tipo):
    moedas_validas = ["USD", "EUR", "BRL"]
    while True:
        moeda = input(f"Digite a moeda de {tipo} (USD, EUR, BRL): ").upper()
        if moeda in moedas_validas:
            return moeda
        else:
            print("Moeda inválida. Tente novamente.")

# Função principal do programa que controla a repetição
def realizar_conversao():
    while True:
        # Entrada de dados
        valor = solicitar_valor()  # Solicita o valor de forma segura
        moeda_de = solicitar_moeda("origem")  # Solicita a moeda de origem
        moeda_para = solicitar_moeda("destino")  # Solicita a moeda de destino

        # Chamada da função e exibição do resultado
        resultado = conversor_moeda(valor, moeda_de, moeda_para)
        if isinstance(resultado, str):
            print(resultado)  # Se a resposta for uma string de erro
        else:
            print(f"Valor convertido: {resultado:.2f} {moeda_para}")

        # Pergunta ao usuário se ele deseja realizar outra conversão
        nova_conversao = input("Deseja realizar uma nova conversão? (s/n): ").lower()
        if nova_conversao != 's':
            print("Obrigado por usar o conversor de moedas!")
            break  # Encerra o loop e o programa

# Iniciar a função principal
realizar_conversao()
