#!/usr/bin/env python3
"""
Implementación de Cifrado Híbrido (RSA + AES).
Usa AES-256 para cifrar el archivo y RSA para cifrar la clave AES.
"""

import subprocess
import os
import secrets

def ejecutar_comando(comando):
    subprocess.run(comando, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print("=== DEMOSTRACIÓN DE CIFRADO HÍBRIDO (RSA + AES) ===\n")
    
    mensaje = "Este es un mensaje secreto para el examen de SGSSI."
    with open("mensaje_hibrido.txt", "w") as f:
        f.write(mensaje)
    print(f"[1] Mensaje original creado: {mensaje}")

    if not os.path.exists("rsa_privada.pem"):
        ejecutar_comando(['openssl', 'genpkey', '-algorithm', 'RSA', '-out', 'rsa_privada.pem', '-pkeyopt', 'rsa_keygen_bits:2048'])
        ejecutar_comando(['openssl', 'rsa', '-pubout', '-in', 'rsa_privada.pem', '-out', 'rsa_publica.pem'])
        print("[2] Par de claves RSA generado.")
    else:
        print("[2] Usando claves RSA existentes.")

    clave_aes = secrets.token_hex(32)
    iv = '0' * 32
    print(f"[3] Clave AES simétrica generada (hex): {clave_aes[:10]}...")

    ejecutar_comando([
        'openssl', 'enc', '-aes-256-cbc', '-in', 'mensaje_hibrido.txt', 
        '-out', 'mensaje.enc', '-K', clave_aes, '-iv', iv
    ])
    print("[4] Mensaje cifrado con AES -> mensaje.enc")

    with open("clave_aes_temp.txt", "w") as f:
        f.write(clave_aes)
    
    ejecutar_comando([
        'openssl', 'pkeyutl', '-encrypt', '-pubin', '-inkey', 'rsa_publica.pem',
        '-in', 'clave_aes_temp.txt', '-out', 'clave_aes.enc'
    ])
    print("[5] Clave AES cifrada con RSA -> clave_aes.enc")

    print("\n=== INICIANDO DESCIFRADO ===")

    ejecutar_comando([
        'openssl', 'pkeyutl', '-decrypt', '-inkey', 'rsa_privada.pem',
        '-in', 'clave_aes.enc', '-out', 'clave_aes_recuperada.txt'
    ])
    with open("clave_aes_recuperada.txt", "r") as f:
        clave_recuperada = f.read().strip()
    print(f"[6] Clave AES recuperada con RSA: {clave_recuperada[:10]}...")

    ejecutar_comando([
        'openssl', 'enc', '-d', '-aes-256-cbc', '-in', 'mensaje.enc',
        '-out', 'mensaje_final.txt', '-K', clave_recuperada, '-iv', iv
    ])
    
    with open("mensaje_final.txt", "r") as f:
        mensaje_final = f.read()
    
    print(f"[7] Mensaje final descifrado: {mensaje_final}")
    
    if mensaje == mensaje_final:
        print("\n✅ ÉXITO: El mensaje original y el descifrado coinciden perfectamente.")
    else:
        print("\n❌ ERROR: Los mensajes no coinciden.")

    os.remove("clave_aes_temp.txt")
    os.remove("clave_aes_recuperada.txt")

if __name__ == "__main__":
    main()
