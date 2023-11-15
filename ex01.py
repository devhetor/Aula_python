import ipaddress

# Função para verificar se um endereço IP é válido
def validar_endereco_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Função para ler o arquivo de entrada e separar endereços válidos e inválidos
def verificar_enderecos(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida_validos:
        enderecos = entrada.read().split()
        enderecos_validos = []
        enderecos_invalidos = []

        for endereco in enderecos:
            if validar_endereco_ip(endereco):
                enderecos_validos.append(endereco)
            else:
                enderecos_invalidos.append(endereco)

        saida_validos.write("[Endereços válidos:] " + ' '.join(enderecos_validos) + '\n')
        saida_validos.write("[Endereços inválidos:] " + ' '.join(enderecos_invalidos))  

# Chamar a função para verificar os endereços
verificar_enderecos('arquivo_entrada.txt', 'arquivo_saida.txt')
