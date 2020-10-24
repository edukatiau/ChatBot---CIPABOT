# Desenvolvido por The Ducks - SESI SENAI SAPUCAIA DO SUL
start = input()

# pega as informações
while(True):
    # pega o id do funcionario
    while(True):
        ID = int(input("Olá, primeiro informe seu ID de Funcionário: "))
        if (11111111 <= ID <= 99999999):
            break
        else:
            print("Informe um ID existente.")
    
    # inicializa o reporte
    emergencia = input("\nQual a sua emergência?\n A - Trabalhador passou mal\n B - Manutenção em Máquina ")
    emergencia = emergencia.lower()
    humano = "a"
    manutencao = "b"

    # se caso for um trabalhador que passou mal
    if emergencia == humano:
        emergencia = "Trabalhador que passou mal"
        gravidade = input("Qual a gravidade do acidente com o trabalhador?\n A - Leve\n B - Moderado\n C - Grave ")
        gravidade = gravidade.lower()
        if gravidade == "a":
            gravidade = "Leve"
        if gravidade == "b":
            gravidade = "Moderado"
        if gravidade == "c":
            gravidade = "Grave"
        print("\nEstamos enviando o relatório a CIPA\n")
            
     # se caso for uma manutenção em uma máquina
    if emergencia == manutencao:
        emergencia = "Manutenção"
        pessoa = input("Envolve acidente com fator humano?\n S - Sim\n N - Não ")
        pessoa = pessoa.lower()
        if pessoa == "s":
            pessoa = "Sim"
        if pessoa == "n":
            ferragens = "Não"
        fogo = input("Existe algum foco de incêndio na região do acidente?\n S - Sim\n N - Não ")
        fogo = fogo.lower()
        if fogo == "s":
            fogo = "Sim"
        if fogo == "n":
            fogo = "Não"
        print("\n Estamos enviando o relatório a CIPA.\n")
        
    # printa as informações à CIPA
    print("##################")
    print("\nDados recolhidos:\n")
    print("Emergência: " + emergencia)
    if (emergencia == "Trabalhador que passou mal"):
        print("Gravidade: " + gravidade)
    if (emergencia == "Manutenção"):
        print("Fator Humano na máquina: " + pessoa)
        print("Fogo na região: " + fogo)
    print("ID: " + str(ID))
