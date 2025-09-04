 
from gtts import gTTS
import os


def texto_a_voz(texto: str, archivo_salida: str = "salida.mp3", idioma: str = "es") -> str:
	"""Convierte texto a voz usando gTTS y guarda un MP3.

	Args:
		texto: Texto a convertir.
		archivo_salida: Nombre del archivo MP3 de salida.
		idioma: Código de idioma (e.g., 'es', 'en').

	Returns:
		Ruta del archivo generado.
	"""
	if not texto or not texto.strip():
		raise ValueError("El texto no puede estar vacío.")

	tts_frances = gTTS(text=texto, lang='fr-fr')
	tts_frances.save(archivo_salida)
	return os.path.abspath(archivo_salida)


if __name__ == "__main__":
	texto = "Bonjour, ceci est un exemple de conversion de texte en parole avec g T T S."
	mp3_path = texto_a_voz(texto, "voz.mp3", "fr-fr")
	print(f"Archivo generado: {mp3_path}")

	
	try:
		os.startfile(mp3_path)  
	except Exception as e:
		print(f"No se pudo reproducir automáticamente: {e}")
