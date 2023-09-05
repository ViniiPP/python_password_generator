# Desenvolvido por ViniiPP (iniciante na área ^_~)
# Gerador de Senhas aleatório em Python, só executar o código
# Todas as senhas serão salvas em um arquivo "senhas.json"
import random
import json
opc = "S"
while (opc == "S"):
    loc = input("Para qual app será a senha? ").upper()
    num = int(input("Digite o tamanho da senha: "))

    adds=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '!','@','#','$','%','&','*','^','/',
        '0','1','2','3','4','5','6','7','8','9']

    senha = ''
    for i in range(num):
        senha += random.choice(adds)

    nome_arquivo = "senhas.json"
    # Tente abrir o arquivo JSON existente se ele existir
    try:
        with open(nome_arquivo, "r") as arquivo_json:
            dados_existente = json.load(arquivo_json)
    except FileNotFoundError:
        dados_existente = {}

    # Adicione a nova senha à lista associada ao aplicativo
    if loc in dados_existente:
        dados_existente[loc].append(senha)
    else:
        dados_existente[loc] = [senha]

    # Escreva todos os dados de volta no arquivo JSON
    with open(nome_arquivo, "w") as arquivo_json:
        json.dump(dados_existente, arquivo_json, indent=4)


    print("-" * 150)
    print("Senha gerada aleatoriamente para {} é: {}".format(loc, senha))
    print("Sua senha contém {} caracteres!".format(num))
    print(f"A senha foi salva no arquivo '{nome_arquivo}'.")
    print("-" * 150)
    opc = input("Deseja fazer outra operação? Sim[S] Não[N]: ").upper()