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

def crear_candidatos():

    candidatos = []

    return candidatos


# ==========================
# REGLA 1
# MAYÚSCULAS
# ==========================

def regla_mayusculas(banco, candidatos):

    for elemento in banco:

        candidatos.append(elemento.upper())

    return candidatos


# ==========================
# REGLA 2
# MINÚSCULAS
# ==========================

def regla_minusculas(banco, candidatos):

    for elemento in banco:

        candidatos.append(elemento.lower())

    return candidatos


# ==========================
# REGLA 3
# CAPITALIZAR
# ==========================

def regla_capitalizar(banco, candidatos):

    for elemento in banco:

        candidatos.append(elemento.capitalize())

    return candidatos
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

    print(f"Elementos encontrados: {len(banco)}\n")

    opcion = mostrar_menu()

   # candidatos = crear_candidatos()

    print(f"\nRegla seleccionada: {opcion}")

 #   if opcion == "1":
#
  #      candidatos = regla_mayusculas(banco, candidatos)
#
   # if opcion == "2":
#
    #    candidatos = regla_minusculas(banco, candidatos)
#
   # if opcion == "3":
#
    #    candidatos = regla_capitalizar(banco, candidatos)
#
   # if opcion == "0":
#
    #    candidatos = regla_mayusculas(banco, candidatos)
    #    candidatos = regla_minusculas(banco, candidatos)
     #   candidatos = regla_capitalizar(banco, candidatos)

    candidatos = generar_combinaciones(banco)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as archivo:

        for elemento in sorted(candidatos):

            archivo.write(elemento + "\n")
#    for elemento in sorted(candidatos):

 #       print(elemento)


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
