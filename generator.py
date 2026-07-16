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
# LECTURA DEL BANCO
# ==========================

def leer_banco():

    banco = []

    with open(INPUT_FILE, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            elemento = linea.strip()

            if elemento:

                banco.append(elemento)

    return banco


# ==========================
# MENÚ
# ==========================

def mostrar_menu():

    print("Seleccione las reglas que desea aplicar:\n")

    print("[1] Mayúsculas")
    print("[2] Minúsculas")
    print("[3] Capitalizar")
    print()
    print("[0] Aplicar TODAS las reglas")
    print()

    opcion = input("Seleccione una opción: ")

    return opcion


# ==========================
# CREAR CANDIDATOS
# ==========================



# ==========================
# REGLA 1
# MAYÚSCULAS
# ==========================

def regla_mayusculas(banco, banco_transformado):

    for elemento in banco:

        banco_transformado.append(elemento.upper())

    return banco_transformado


# ========================# REGLA 2
# MINÚSCULAS
# ==========================

def regla_minusculas(banco, banco_transformado):

    for elemento in banco:

        banco_transformado.append(elemento.lower())

    return banco_transformado


# ==========================
# REGLA 3
# CAPITALIZAR
# ==========================

def regla_capitalizar(banco, banco_transformado):

    for elemento in banco:

        banco_transformado.append(elemento.capitalize())

    return banco_transformado
# ==========================
# MOTOR DE COMBINACIONES
# PROFUNDIDAD 4
# ==========================

def generar_combinaciones(banco):

    candidatos = []

    for primero in banco:

        # -------------------------
        # PROFUNDIDAD 1
        # -------------------------

        candidatos.append(primero)

        for segundo in banco:

            if segundo in [primero]:

                continue

            # -------------------------
            # PROFUNDIDAD 2
            # -------------------------

            candidatos.append(
                primero + segundo
            )

            for tercero in banco:

                if tercero in [primero, segundo]:

                    continue

                # -------------------------
                # PROFUNDIDAD 3
                # -------------------------

                candidatos.append(
                    primero +
                    segundo +
                    tercero
                )

                for cuarto in banco:

                    if cuarto in [primero, segundo, tercero]:

                        continue

                    # -------------------------
                    # PROFUNDIDAD 4
                    # -------------------------

                    candidatos.append(
                        primero +
                        segundo +
                        tercero +
                        cuarto
                    )

    return candidatos




# ==========================
# PROGRAMA PRINCIPAL
# ==========================

def main():

    banner()

    banco = leer_banco()
    banco_transformado = []
    print(f"Elementos encontrados: {len(banco)}\n")

    opcion = mostrar_menu()

    print(f"\nRegla seleccionada: {opcion}")

    if opcion == "1":

      banco_transformado = regla_mayusculas(
        banco,
        banco_transformado
      )

    if opcion == "2":

       banco_transformado = regla_minusculas(
        banco,
        banco_transformado
       )

    if opcion == "3":

       banco_transformado = regla_capitalizar(
        banco,
        banco_transformado
       )

    if opcion == "0":


       banco_transformado = regla_mayusculas(
        banco,
        banco_transformado
       )

       banco_transformado = regla_minusculas(
        banco,
        banco_transformado
       )

       banco_transformado = regla_capitalizar(
        banco,
        banco_transformado
       )


    banco_transformado = list(dict.fromkeys(banco_transformado))

    candidatos = generar_combinaciones(banco_transformado)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as archivo:

        for elemento in sorted(candidatos):

            archivo.write(elemento + "\n")



    print("\n=========================================")
    print("Diccionario generado correctamente.")
    print(f"Candidatos generados: {len(candidatos)}")
    print(f"Archivo creado: {OUTPUT_FILE}")
    print("=========================================")

# ==========================
# INICIO DEL PROGRAMA
# ==========================

if __name__ == "__main__":
    main()
