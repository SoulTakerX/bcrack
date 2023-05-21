import bcrypt

hashed_password = input("Digite a hash da senha: ")


art = '''
\033[1;31m _                         _    \033[0m
\033[1;31m| |__   ___ _ __ __ _  ___| | __\033[0m
\033[1;31m| '_ \ / __| '__/ _` |/ __| |/ /\033[0m
\033[1;31m| |_) | (__| | | (_| | (__|   < \033[0m
\033[1;31m|_.__/ \___|_|  \__,_|\___|_|\_\033[0m
'''

wordlist_file = input("Digite o caminho para o arquivo de wordlist: ")
verbose_mode = input("Ativar o modo verbose? (S/N): ").lower() == "s"

print(art) 

with open(wordlist_file, "r") as file:
    for line in file:
        word = line.strip()  # Remove espaços em branco e quebras de linha
        if bcrypt.checkpw(word.encode('utf-8'), hashed_password.encode('utf-8')):
            print(f"A senha encontrada é: {word}")
            break
        elif verbose_mode:
            print(f"Senha negada: {word}")

    else:
        print("A senha não foi encontrada no arquivo.")
