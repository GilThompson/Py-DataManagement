import os
import pandas as pd

def excel_to_csv(input_path, output_path):
    # Verificar si la carpeta de salida existe, si no, crearla
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Obtener una lista de archivos Excel en el directorio de entrada
    excel_files = [f for f in os.listdir(input_path) if f.endswith('.xlsx')]

    for excel_file in excel_files:
        excel_path = os.path.join(input_path, excel_file)
        csv_file = os.path.splitext(excel_file)[0] + '.csv'
        csv_path = os.path.join(output_path, csv_file)

        # Leer el archivo Excel y guardarlo como CSV
        df = pd.read_excel(excel_path)
        df.to_csv(csv_path, index=False)
        print(f'{excel_file} convertido a {csv_file}')

if __name__ == "__main__":
    input_directory = "D:/Dropbox (RSG)/2023/02- Airplane/03- Results/Thermal_Calibration_Results/Thermal_Calibration_Results"  # Ruta al directorio de entrada con archivos Excel
    output_directory = "D:/Dropbox (RSG)/2023/02- Airplane/03- Results/Thermal_Calibration_Results/Thermal_Calibration_Results"  # Ruta al directorio donde se guardarán los archivos CSV
    excel_to_csv(input_directory, output_directory)
