 
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

	tts = gTTS(text=texto, lang=idioma)
	tts.save(archivo_salida)
	return os.path.abspath(archivo_salida)


if __name__ == "__main__":
	texto = "Hola, este es un ejemplo de conversión de texto a voz con g T T S."
	mp3_path = texto_a_voz(texto, "voz.mp3", "es")
	print(f"Archivo generado: {mp3_path}")

	# Intentar reproducir automáticamente en Windows (opcional)
	try:
		os.startfile(mp3_path)  # Solo funciona en Windows
	except Exception as e:
		print(f"No se pudo reproducir automáticamente: {e}")
