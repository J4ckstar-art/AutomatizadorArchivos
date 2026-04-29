#Importo el o (Operating System) y el shutil (SShell Utilities)
import os
import shutil

#Defino las reglas 
def organizar_escritorio(ruta):
    formatos = {
        "Documentos": [".pdf", ".docx", ".txt"],
        "Imagenes": [".jpg", ".png", ".jpeg"],
        "Instaladores": [".exe", ".msi"],
        "Musica": [".mp3", ".wav"]
    }
    #Bucle principal donde leera y definira cada archivo para ser organiado
    for archivo in os.listdir(ruta):
        nombre, extension = os.path.splitext(archivo)

        #Verificacion y clasificacion
        for carpeta, lista_ext in formatos.items():
            if extension.lower() in lista_ext:

                #Creacion de carpeta y mover los archivos
                destino = os.path.join(ruta, carpeta)
                os.makedirs(destino, exist_ok=True)
                shutil.move(os.path.join(ruta, archivo), os.path.join(destino, archivo))

#Ruta de la carpeta donde se almacenen los archivos (se coloca el "." para que el script entienda que debe trabajar en la carpeta donde está guardado el archivo .py)
organizar_escritorio(".")

#Por ultimo al abrir la terminal se debe ejecutar el comando: "python organizador.py" y se veran las carpetas junto con los archivos corrrespondientes  