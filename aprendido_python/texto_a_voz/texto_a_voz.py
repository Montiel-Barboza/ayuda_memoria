# Instalar: pip install gTTS playsound
# gTTS (Google Text-to-Speech) convierte texto en un archivo de audio (ej: .mp3)
# playsound reproduce archivos de audio simples.
from gtts import gTTS
from playsound import playsound
import os


def texto_a_voz(texto, idioma='es', nombre_archivo='salida.mp3'):
    """
    Convierte un texto a voz y lo reproduce.

    :param texto: El texto que se desea convertir a voz.
    :param idioma: El idioma del texto (por defecto es 'es' para español).
    :param nombre_archivo: El nombre del archivo de salida (por defecto es 'salida.mp3').
    """
    # Crear el objeto gTTS
    tts = gTTS(text=texto, lang=idioma)

    # Guardar el archivo de audio
    tts.save(nombre_archivo)

    # Reproducir el archivo de audio
    playsound(nombre_archivo)
    # os.system('start ' + nombre_archivo)  # Alternativa para Windows

    # Eliminar el archivo de audio después de reproducirlo
    os.remove(nombre_archivo)


if __name__ == "__main__":
    texto = "Acá se escribe el texto que se desea convertir a voz."
    texto_a_voz(texto)
    