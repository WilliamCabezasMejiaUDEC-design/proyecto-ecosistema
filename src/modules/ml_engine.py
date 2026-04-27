import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def run_ml_analysis(csv_path):
    """
    Motor de análisis de datos para el Ecosistema 4R+T.
    Realiza limpieza, clustering y visualización de tendencias.
    """
    try:
        # 1. Carga y Limpieza Quirúrgica
        df = pd.read_csv(csv_path)
        
        # Estandarización de nombres para evitar errores
        col_rec = 'Toneladas_Recolectadas_Historico (Emserfusa)'
        col_proy = 'Toneladas_Proyectadas (Urbana)'
        
        # Conversión de fecha
        df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
        
        # Imputación de nulos (Estrategia: Media para mantener la tendencia histórica)
        if col_rec in df.columns:
            df[col_rec] = df[col_rec].fillna(df[col_rec].mean())

        # 2. Preparación para ML (Selección de columnas numéricas)
        data_numeric = df[[col_rec, col_proy]].dropna()
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(data_numeric)

        st.markdown("## 🧠 Evidencia Analítica: Machine Learning")

        # 3. Clustering (K-Means)
        st.subheader("Clustering de Eficiencia de Recolección")
        kmeans = KMeans(n_clusters=3, n_init=10).fit(X_scaled)
        
        # Visualización PCA (Reducción a 2D)
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(X_scaled)
        
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.set_facecolor('#000000')
        fig.patch.set_facecolor('#000000')
        scatter = ax.scatter(pca_result[:,0], pca_result[:,1], c=kmeans.labels_, cmap='viridis')
        ax.set_title("Agrupamiento de Comportamiento Histórico", color='white')
        ax.tick_params(colors='white')
        st.pyplot(fig)

        st.success("Análisis completado: Se identificaron 3 patrones de recolección en el histórico.")

    except Exception as e:
        st.error(f"Error en el motor de ML: {e}")
        st.info("Asegúrate de que el archivo CSV tenga los nombres de columna correctos.")