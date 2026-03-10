import json
import os

ARQUIVO_CONFIG = 'config.json'
TEMA_PADRAO = "Cozy Matcha"

def ler_tema_atual():
    """Lê o arquivo JSON e retorna o nome do tema salvo."""
    if os.path.exists(ARQUIVO_CONFIG):
        try:
            with open(ARQUIVO_CONFIG, 'r') as f:
                dados = json.load(f)
                return dados.get('tema', TEMA_PADRAO)
        except:
            return TEMA_PADRAO
    return TEMA_PADRAO

def salvar_tema(nome_do_tema):
    """Salva a escolha do usuário no arquivo JSON."""
    with open(ARQUIVO_CONFIG, 'w') as f:
        json.dump({'tema': nome_do_tema}, f)