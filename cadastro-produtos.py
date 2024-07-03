# Dictionary
# Chave -> valor
"""Cadastro de produto"""
#__Version__ "0.1.0"


# Criando um dicionario
produto = {
    "nome": "Caneta ",
    "cores": ["azul", "branco"], # Lista dentro do dicionario
    "preco": 3.23,
    "dimensao": { # Dicionario dentro de dicionario
        "altura": 12.15,
        "lagura": 1.5,
    },
    "em_estoque": True,
    "codigo": 100589,
    "codebar":None,
}
cliente = {
    "nome": "Manoel"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 7
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]
print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f"e pagou o total de R$ {total_compra}."
)
