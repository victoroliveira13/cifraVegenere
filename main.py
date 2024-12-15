def vigenere_encode(msg, key):
    msg = msg.upper()
    key = key.upper()

    resultado = []
    key_index = 0

    print("Mensagem + Chave:")
    for char in msg:
        print(f"{char} (", end="")

        if char.isalpha():
            letra_msg = ord(char) - ord('A')
            letra_key = ord(key[key_index]) - ord('A')

            print(f"{letra_msg}) + {key[key_index]} ({letra_key}) = ", end="")

            letra_cifrada = (letra_msg + letra_key) % 26
            resultado.append(chr(letra_cifrada + ord('A')))

            print(f"{letra_cifrada} -> {chr(letra_cifrada + ord('A'))}")

            key_index = (key_index + 1) % len(key)
        else:
            resultado.append(char)
            print("- Ignorado")

    print("\nResultado:")
    resultado_final = ''.join(resultado)
    print(resultado_final)
    return resultado_final


def vigenere_decode(msg, key):
    msg = msg.upper()
    key = key.upper()

    resultado = []
    key_index = 0

    print("Mensagem - Chave:")
    for char in msg:
        print(f"{char} (", end="")

        if char.isalpha():
            letra_msg = ord(char) - ord('A')
            letra_key = ord(key[key_index]) - ord('A')

            print(f"{letra_msg}) - {key[key_index]} ({letra_key}) = ", end="")

            letra_decifrada = (letra_msg - letra_key) % 26
            resultado.append(chr(letra_decifrada + ord('A')))

            print(f"{letra_decifrada} -> {chr(letra_decifrada + ord('A'))}")

            key_index = (key_index + 1) % len(key)
        else:
            resultado.append(char)
            print("- Ignorado")

    print("\nResultado:")
    resultado_final = ''.join(resultado)
    print(resultado_final)
    return resultado_final


# Testando as funções
if __name__ == "__main__":
    txt1 = "senha"
    txt2 = "chave"

    print("\n==== Codificando ====\n")
    texto_cifrado = vigenere_encode(txt1, txt2)

    print("\n==== Decodificando ====\n")
    vigenere_decode(texto_cifrado, txt2)