import json


def carregar_mangas():
    try:
        with open("mangas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_mangas(mangas):
    with open("mangas.json", "w", encoding="utf-8") as arquivo:
        json.dump(mangas, arquivo, ensure_ascii=False, indent=2)


def pedir_titulo():
    while True:
        titulo = input("Título: ").strip()
        if not titulo:
            print("O título não pode ficar vazio, tente novamente.")
        else:
            return titulo


def pedir_numero(mensagem, minimo, maximo):
    while True:
        try:
            try:
                numero = int(input(mensagem))
            except ValueError:
                raise ValueError("Digite um número válido")
            if numero < minimo:
                raise ValueError(f"O número precisa ser pelo menos {minimo}")
            if numero > maximo:
                raise ValueError(f"O número não pode ser maior que {maximo}")
            return numero
        except ValueError as e:
            print("Erro:", e)


def pedir_status():
    while True:
        try:
            status = input("Status (Lendo/Quero ler/Lido/Para ser lido): ").strip().lower()
            if status not in ["lendo", "quero ler", "lido", "para ser lido"]:
                raise ValueError("Status inválido, escolha uma das opções")
            return status
        except ValueError as e:
            print("Erro:", e)

def adicionar_manga():
    titulo = pedir_titulo()
    volume_total = pedir_numero("Volume total: ", 1, 10000)
    volume_atual = pedir_numero("Volume atual: ", 0, volume_total)
    status = pedir_status()

    mangas = carregar_mangas()

    novo = {
            "titulo": titulo,
            "volume_atual": volume_atual,
            "volume_total": volume_total,
            "status": status,
            }

    mangas.append(novo)
    salvar_mangas(mangas)

    print()
    print("Mangá adicionado com sucesso!\n")
        

def listar_mangas():
    print()
    mangas = carregar_mangas()
    if not mangas:
            print("Nenhum mangá cadastrado ainda.\n")
            return
    for manga in mangas:
        faltam = manga["volume_total"] - manga["volume_atual"]
        print(f"- {manga['titulo']}: volume ({manga['volume_atual']}/{manga['volume_total']}), faltam {faltam} - {manga['status']}")
    print()

def remover_manga():
    mangas = carregar_mangas()
    if not mangas:
        print("Nenhum mangá cadastrado ainda.\n")
        return

    print()
    print("Qual mangá você quer remover?")
    for estado in range(len(mangas)):
        print(f"{estado+1}. {mangas[estado]['titulo']}") 

    while True:
        try:
            try:
                resposta = int(input("Número: "))
            except ValueError:
                raise ValueError("Não é um número, tente novamente")
            if resposta < 1 or resposta > len(mangas):
                raise ValueError("Número inválido, tente novamente")
            break
        except ValueError as e:
            print("Erro:", e)

    removido = mangas.pop(resposta - 1)

    salvar_mangas(mangas)
    print()
    print(f"{removido['titulo']} removido com sucesso!")
    print()

while True:
    try:
        try:
            print("Escolha um número\n1. Adicionar mangá\n2. Listar mangás\n3. Remover mangá\n4. Sair")
            numero = int(input())
        except ValueError:
            raise ValueError("Não é um número, tente novamente")

        if numero < 1 or numero > 4:
            raise ValueError("O número não está nas opções, tente novamente")

    except ValueError as e:
        print("Erro:", e)
        continue

    if numero == 1:
        adicionar_manga()
    elif numero == 2:
        listar_mangas()
    elif numero == 3:
        remover_manga()
    elif numero == 4:
        break