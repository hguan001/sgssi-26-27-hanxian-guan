def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            nuevo_caracter = chr((ord(caracter) - ascii_offset - desplazamiento) % 26 + ascii_offset)
            resultado += nuevo_caracter
        else:
            resultado += caracter
    return resultado

mensaje_cifrado = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"

print("Iniciando ataque de fuerza bruta...\n")
for clave in range(1, 26):
    texto_descifrado = descifrar_cesar(mensaje_cifrado, clave)
    print(f"Clave {clave:02d}: {texto_descifrado}")
