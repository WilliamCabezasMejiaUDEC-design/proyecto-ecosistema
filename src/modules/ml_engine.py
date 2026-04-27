import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

def run_ml_analysis(csv_path, target_col='riesgo'):
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        st.error(f"Error cargando datos: {e}")
        return

    num_df = df.select_dtypes(include=['float64', 'int64'])
    X = num_df.drop(columns=[target_col], errors='ignore')
    y = num_df[target_col] if target_col in num_df.columns else None

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    st.markdown("## 🧠 Evidencia Analítica: ML")

    # PCA + K-Means
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(X_scaled)
    kmeans = KMeans(n_clusters=3, n_init=10).fit(X_scaled)
    
    fig, ax = plt.subplots(figsize=(6, 3))
    fig.patch.set_facecolor('#080808')
    ax.set_facecolor('#121212')
    ax.scatter(pca_result[:,0], pca_result[:,1], c=kmeans.labels_, cmap='viridis')
    st.pyplot(fig)

    # Clasificación
    if y is not None:
        X_tr, X_te, y_tr, y_te = train_test_split(X_scaled, y, test_size=0.2)
        model = RandomForestClassifier().fit(X_tr, y_tr)
        preds = model.predict(X_te)
        st.metric("Accuracy del Modelo", f"{accuracy_score(y_te, preds):.2%}")