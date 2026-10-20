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