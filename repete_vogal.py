words = []
while True:
    word = input("Digite uma palavra (ou enter para sair): ").strip()
    if not word: # Condição de parada
        break

    final_word = ""
    for letter in word:
        # TODO: remover acentuação usando funções
        if letter.lower() in "aeiouãêéóíá":
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

print(*words, sep="\n")



