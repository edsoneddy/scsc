def process_text():
    words = set()  # Usamos un set para almacenar palabras únicas
    pending_word = ""  # Para manejar palabras que continúan en la siguiente línea
    
    try:
        while True:
            try:
                line = input().strip()
                
                # Si la línea está vacía, procesamos la palabra pendiente si existe
                if not line and pending_word:
                    words.add(pending_word.lower())
                    pending_word = ""
                    continue
                
                # Dividir la línea en palabras
                current_words = line.split()
                
                if not current_words:
                    continue
                    
                # Procesar cada palabra en la línea
                for i, word in enumerate(current_words):
                    # Eliminar puntuación al final de la palabra
                    word = word.rstrip('.,')
                    
                    # Caso 1: Tenemos una palabra pendiente
                    if pending_word:
                        if word.endswith('-'):
                            # La palabra sigue continuando
                            pending_word += word[:-1]
                        else:
                            # La palabra termina aquí
                            complete_word = pending_word + word
                            words.add(complete_word.lower())
                            pending_word = ""
                    
                    # Caso 2: Nueva palabra que puede continuar
                    elif word.endswith('-'):
                        if i == len(current_words) - 1:  # Si es la última palabra de la línea
                            pending_word = word[:-1]
                        else:
                            # Es un guión que forma parte de la palabra
                            words.add(word.lower())
                    
                    # Caso 3: Palabra normal
                    else:
                        # Verificar si es una palabra válida (contiene letras)
                        if any(c.isalpha() for c in word):
                            words.add(word.lower())
                
            except EOFError:
                # Si hay una palabra pendiente al final del archivo, la agregamos
                if pending_word:
                    words.add(pending_word.lower())
                break
    
        # Convertir guiones de continuación en el medio de las palabras
        final_words = set()
        for word in words:
            if '-' in word and not word.endswith('-'):
                # Agregar tanto la versión con guión como sin guión
                final_words.add(word)
                final_words.add(word.replace('-', ''))
            else:
                final_words.add(word)
        
        # Ordenar e imprimir las palabras
        for word in sorted(final_words):
            print(word)
            
    except EOFError:
        pass

# Ejecutar el programa
process_text()