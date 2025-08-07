import json

CAMINHO_ARQUIVO = "historico.json"

def salvar_historico(historico):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, indent=4)

def carregar_historico():
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
