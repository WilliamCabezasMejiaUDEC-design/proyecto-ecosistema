import pandas as pd
import os

def get_kpi_summary():
    # Aseguramos la ruta al archivo
    file_path = os.path.join("data", "datos_4RT_historico.csv")
    
    if not os.path.exists(file_path):
        return "Error: Base de datos no encontrada."

    df = pd.read_csv(file_path)
    col = 'Toneladas_Recolectadas_Historico (Emserfusa)'
    
    # Cálculos simples
    promedio = df[col].mean()
    total_registros = len(df)
    
    # Lógica de Radar (Alerta)
    alerta = "✅ Todo normal."
    if df[col].iloc[-1] < (promedio * 0.9): # Si el último dato es < 90% del promedio
        alerta = "⚠️ ALERTA: La recolección está por debajo del umbral."
        
    return f"📊 *Resumen 4R+T*\n- Promedio: {promedio:.2f} Ton\n- Registros: {total_registros}\n- Estado: {alerta}"