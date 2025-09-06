import os
from report_generator import ReporteVentas

# Definir la ruta del archivo Excel y el directorio de salida
EXCEL_FILE = "sales_data.xlsx"
OUTPUT_DIR = "reportes_automatizados"

if __name__ == "__main__":
    # Crear el directorio de salida si no existe
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Diagnóstico: mostrar directorio actual y archivos
    print("Directorio actual:", os.getcwd())
    print("Archivos en el directorio:", os.listdir())

    print("Iniciando el proceso de generación de reporte de ventas...")
    try:
        # Instanciar la clase ReporteVentas
        reporte = ReporteVentas(EXCEL_FILE, OUTPUT_DIR)

        # Ejecutar el método principal que orquesta todo el proceso
        reporte.generar_reporte()

        print("\n✅ Proceso completado exitosamente.")

    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        print(f"Asegúrate de que el archivo '{EXCEL_FILE}' exista en la misma carpeta.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado: {e}")