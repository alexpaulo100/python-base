#String
#Interpolação
# Formatações de strings
# Concatenação %s usar em logging
# str.format{} usar em mensagens longas, exemplo emails
# f-strings usar em todo restante, mensagens, prints, errors


#__version__ = "0.1.1"
#__author__ = "Alex
import sys
import os



arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)# emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt

template_content = open(templatepath).read()


for line in open(filepath):
    name, email = line.split(",")
    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print("-=-=-" *10)
    # Define os valores para substituição
    valores = {
        "nome": name,
        "produto": "caneta",
        "texto": "Ótima qualidade de escrita",
        "link": "http://canetassos.com",
        "quantidade": 1,
        "preco": 48.98,
    }

# Substitui os marcadores de posição no modelo
email_formatado = template_content.format(**valores)

# Imprime o email formatado
print(email_formatado)

print("-----"*10)



    
    
    
    
"""   
    print(
        open(templatepath).read()
        % {
            "nome":name,
            "produto": "caneta",
            "texto": "Ótima qualidade de escrita",
            "link":"http//canetassos.com",
            "quantidade" : 1,
            "preco": 48.98,
        }
    )

print("---" *10)

"""