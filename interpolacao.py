#String
#Interpolação
# Formatações de strings
# Concatenação %s usar em logging
# str.format{} usar em mensagens longas, exemplo emails
# f-strings usar em todo restante, mensagens, prints, errors

#__version__ = "0.1.0"
#__author__ = "Alex



email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Este produto é ótimo para resolver %(texto)s
Clique agora em %(link)s
Apenas %(quantidade)d disponiveis!
Preço promocional %(preco).2f
"""
clientes = ["Maria", "Joao", "Alex"]

for cliente in clientes:
    print(email_tmpl % {"nome": cliente, "produto":"caneta", "texto": "Escrever muito bem", 
    "link":"www.canetaslegais.com","quantidade": 2,"preco":50.5,}
)
    
# New style format
print("=" * 20)
email_tmpl2 = """
Olá, {nome}
Tem interesse em comprar {produto}?
Este produto é ótimo para resolver {texto}
Clique agora em {link}
Apenas {quantidade} disponiveis!
Preço promocional: R${preco:.2f}
"""


clientes = ["Marta", "Jose", "Alexandre"]

for cliente in clientes:
    print(email_tmpl2.format(nome=cliente, produto="caneta", texto="Escrever muito bem",
            link="www.canetaslegais.com", quantidade=2, preco= 50.5))

# Assim com f string é a forma mais moderna de formatar strings
produto = "caneta"
preco = 50.50
print(f"Cliente {cliente}, obrigado por comprar a {produto} conosco e pagar R${preco:.2f}.")

# Unicode explorer emojis
print("\N{panda face}")
