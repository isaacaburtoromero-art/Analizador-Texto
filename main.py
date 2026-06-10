texto_original = """
Hola mundo. Esto es una prueba de programación en Python.
Python es genial, y la programación nos ayuda a resolver probelmas lógicos.
Hola de nuevo, mundo de Python
"""

print ("--- Texto Original ---")
print (texto_original)
print("-" * 30)

texto_bajo = texto_original.lower()

signos=[".", ",", "!", "?", ";", "!", "\n"]
for signo in signos:
    texto_limpio = texto_bajo.replace(signo, "")

    print ("\n--- FASE 1: TEXTO LIMPIO ---")
    print (texto_limpio)
    print ("-" * 30)

    lista_palabras = texto_limpio.split()
    print ("\n--- FASE 2: LISTA DE PALABRAS ---")
    print (lista_palabras)
    print ("-" * 30)

    frecuencias = {}

    for palabra in lista_palabras:
        if palabra not in frecuencias:
            frecuencias[palabra] = 1
        else:
            frecuencias[palabra] += 1

    print ("\n--- FASE 3: FRECUENCIAS DE PALABRAS ---")
    print (frecuencias)
    print ("-" * 30)

    palabras_ordenadas =  sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    top_5_palabras = palabras_ordenadas[:5]

    print ("\n--- FASE 4: TOP 5 PALABRAS MÁS FRECUENTES ---")
    for posicion, (palabra, conteo) in enumerate(top_5, 1):
        print(f"{posicion}. {palabra} - {conteo} veces")
        print ("-" * 30)