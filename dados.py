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