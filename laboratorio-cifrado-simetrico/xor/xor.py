# Leer mensaje y clave como cadenas de bytes
mensaje = b"ATAQUE AL AMANECER"
clave = b"CLAVE1234567890123"

# Aplicar XOR byte a byte para obtener el criptograma
criptograma = bytes([m ^ c for m, c in zip(mensaje, clave)])

# Usar la misma operacion XOR para recuperar el mensaje original
descifrado = bytes([c ^ k for c, k in zip(criptograma, clave)])

# Mostrar resultados
print(f"Mensaje original:  {mensaje.decode()}")
print(f"Clave utilizada:   {clave.decode()}")
print(f"Criptograma (hex): {criptograma.hex().upper()}")

# Comprobar que coincide
if mensaje == descifrado:
    print("\nExito: El descifrado coincide exactamente con el mensaje original.")
