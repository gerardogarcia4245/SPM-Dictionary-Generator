#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=========================================================
        SPM Dictionary Generator v1.0
---------------------------------------------------------
 Laboratorio de Pentesting Ético SSPC - UIICOT
 Gerardo García Galarza

 Generador de diccionarios personalizados
 basado en información obtenida durante
 la fase de reconocimiento (OSINT).

 Desarrollo educativo
=========================================================
"""

# ==========================
# CONFIGURACIÓN
# ==========================

INPUT_FILE = "spm_wordlist.txt"
OUTPUT_FILE = "output/spm_dictionary.txt"


# ==========================
# BANNER
# ==========================

def banner():

    print("=" * 57)
    print("        SPM Dictionary Generator v1.0")
    print("=" * 57)
    print()


# ==========================
# LECTURA DEL ARCHIVO BASE
# ==========================

def leer_palabras():

    palabras = []

    with open(INPUT_FILE, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            palabra = linea.strip()

            if palabra:

                palabras.append(palabra)

    return palabras


# ==========================
# MENÚ
# ==========================

def mostrar_menu():

    print("Seleccione las reglas que desea aplicar:\n")

    print("[1] Mayúsculas")
    print("[2] Minúsculas")
    print("[3] Capitalizar")
    print("[4] Agregar años")
    print("[5] Agregar números comunes")
    print("[6] Agregar símbolos")
    print("[7] Año + símbolo")
    print("[8] Símbolo + año")
    print("[9] Leet Speak")
    print("[10] Concatenar palabras")
    print("[11] Concatenar + símbolo")
    print("[12] Concatenar + año")
    print("[13] Concatenar + año + símbolo")
    print()
    print("[0] Aplicar TODAS las reglas")
    print()

    opcion = input("Seleccione una opción: ")

    return opcion

# ==========================
# CREAR DICCIONARIO
# ==========================

def crear_diccionario():

    diccionario = set()

    return diccionario

# ==========================
# REGLA 1
# MAYÚSCULAS
# ==========================

def regla_mayusculas(palabras, diccionario):

    for palabra in palabras:

        diccionario.add(palabra.upper())

    return diccionario






# ==========================
# PROGRAMA PRINCIPAL
# ==========================

def main():

    banner()

    palabras = leer_palabras()

    print(f"Palabras encontradas: {len(palabras)}\n")

    opcion = mostrar_menu()

    diccionario = crear_diccionario()

    print(f"\nRegla seleccionada: {opcion}")
    print(f"Entradas actuales: {len(diccionario)}")    


# ==========================
# INICIO DEL PROGRAMA
# ==========================

if __name__ == "__main__":
    main()
