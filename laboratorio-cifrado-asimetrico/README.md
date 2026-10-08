# Cifrado Híbrido (RSA + AES)

## Objetivo
Implementar un sistema de cifrado híbrido. Dado que RSA solo puede cifrar archivos pequeños, este programa utiliza AES-256 para cifrar el archivo de forma simétrica, y luego utiliza la clave pública RSA para cifrar la clave AES.

## Uso
```bash
python3 cifrado_hibrido.py
