# Função para converter bytes em megabytes
def bytes_para_megabytes(bytes):
    return bytes / (1024 * 1024)

# Função para calcular o percentual de uso
def calcular_percentual(total, uso):
    return (uso / total) * 100

# Leitura do arquivo e armazenamento dos dados
usuarios = []
with open('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        usuario, espaco = linha.split()
        usuarios.append((usuario, int(espaco)))

# Ordenando os usuários pelo espaço ocupado
usuarios.sort(key=lambda x: x[1], reverse=True)

# Criação do relatório
with open('relatorio.txt', 'w') as relatorio:
    relatorio.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    relatorio.write("-" * 60 + "\n")
    relatorio.write("Nr. Usuário     Espaço utilizado    % do uso\n")

    total_uso = sum(espaco for _, espaco in usuarios)
    for i, (usuario, espaco) in enumerate(usuarios, start=1):
        espaco_mb = bytes_para_megabytes(espaco)
        percentual = calcular_percentual(total_uso, espaco)
        relatorio.write(f"{i:<3} {usuario:<15} {espaco_mb:10.2f} MB {percentual:10.2f}%\n")

    relatorio.write(f"\nEspaço total ocupado: {bytes_para_megabytes(total_uso):.2f} MB\n")
    relatorio.write(f"Espaço medio ocupado: {bytes_para_megabytes(total_uso/len(usuarios)):.2f} MB\n")
