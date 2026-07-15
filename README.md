# SPM Dictionary Generator

Generador de diccionarios personalizados para laboratorios de Pentesting Ético.

Proyecto desarrollado con fines educativos para el curso de Pentesting Ético de la SSPC - UIICOT.

---

# Objetivo

Generar diccionarios personalizados a partir de información obtenida durante la fase de reconocimiento (OSINT), simulando el proceso utilizado durante auditorías de seguridad autorizadas.

El proyecto busca enseñar cómo pequeñas piezas de información pública pueden convertirse en miles de candidatos de contraseña.

---

# Características

- Lectura de palabras base.
- Generación automática de variantes.
- Transformaciones de texto.
- Eliminación de duplicados.
- Motor de combinaciones configurable.
- Exportación del diccionario final.

---

# Arquitectura

```
                spm_wordlist.txt
                       │
                       ▼
              Leer palabras base
                       │
                       ▼
      Agregar años y símbolos al banco
                       │
                       ▼
         Aplicar transformaciones
      (Mayúsculas, Minúsculas y Capitalizar)
                       │
                       ▼
          Eliminar palabras duplicadas
                       │
                       ▼
           Banco de candidatos final
                       │
                       ▼
      Generar combinaciones (1 a 4)
                       │
                       ▼
            spm_dictionary.txt
```

---

# Funcionamiento

## Paso 1

El programa carga un archivo denominado:

```
spm_wordlist.txt
```

Ejemplo:

```
Seguridad
Privada
SPM
Control
Recepcion
Monitoreo
```

---

## Paso 2

Se agregan automáticamente elementos comunes utilizados en contraseñas.

### Años

```
2024
2025
2026
2027
```

### Símbolos

```
!
@
#
$
%
&
*
_
```

Con ello se forma el banco inicial de elementos.

---

## Paso 3

Sobre las palabras originales se aplican las transformaciones seleccionadas por el usuario.

Actualmente se implementan:

- Mayúsculas
- Minúsculas
- Capitalizar

Ejemplo:

```
Seguridad

↓

SEGURIDAD

↓

seguridad

↓

Seguridad
```

Los años y símbolos permanecen sin modificaciones.

---

## Paso 4

El programa elimina automáticamente todas las palabras duplicadas.

---

## Paso 5

Se genera el banco definitivo de candidatos.

Ejemplo:

```
Seguridad
SEGURIDAD
seguridad

Privada
PRIVADA
privada

2026

#

$
```

---

## Paso 6

El motor genera automáticamente combinaciones utilizando los elementos del banco.

Profundidad máxima:

- 1 elemento
- 2 elementos
- 3 elementos
- 4 elementos

Ejemplo:

```
SeguridadPRIVADA2026#

SPMControl2025@

seguridadPRIVADA$

ControlSPM2024#
```

Durante esta fase no se repiten elementos dentro de la misma combinación.

---

# Estado del proyecto

## Implementado

- Lectura de archivo
- Menú interactivo
- Mayúsculas
- Minúsculas
- Capitalizar
- GitHub
- Control de versiones

## En desarrollo

- Construcción automática del banco de candidatos
- Eliminación de duplicados
- Motor de combinaciones
- Exportación del diccionario

---

# Tecnologías

- Python 3
- Git
- GitHub
- Kali Linux

---

# Finalidad

Este software fue desarrollado exclusivamente con fines educativos para enseñar la construcción de diccionarios personalizados durante ejercicios de Pentesting Ético y auditorías de seguridad autorizadas.

No debe utilizarse sobre sistemas para los cuales no se cuente con autorización expresa.

---

# Autor

Gerardo García Galarza

Unidad de Inteligencia, Investigación Cibernética y Operaciones Tecnológicas

Secretaría de Seguridad y Protección Ciudadana

México# SPM-Dictionary-Generator
Generador de diccionarios personalizados para laboratorios de Pentesting Ético.
