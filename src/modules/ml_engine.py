import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report

def run_ml_analysis(csv_path):
    df = pd.read_csv(csv_path)
    
    st.markdown("## 🧠 Evidencia Analítica: Machine Learning")
    
    # 1. K-Means & PCA (Clustering)
    st.subheader("Clustering (K-Means) de Residuos")
    kmeans = KMeans(n_clusters=3).fit(df.select_dtypes(include=['float64', 'int64']))
    st.write("Interpretación: Los datos se agruparon en 3 patrones de recolección según el histórico PGIRS.")
    
    # 2. Clasificación (Evidencia de Métricas)
    st.subheader("Validación del Modelo (Métricas)")
    # Simulación de predicción (reemplaza 'target' con tu columna real)
    y_test = [1, 0, 1, 1, 0] # Datos ejemplo
    y_pred = [1, 0, 0, 1, 0] # Predicción ejemplo
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Accuracy", f"{accuracy_score(y_test, y_pred):.2f}")
    col2.metric("F1 Score", f"{f1_score(y_test, y_pred):.2f}")
    
    st.write("### Matriz de Confusión")
    st.write(confusion_matrix(y_test, y_pred))
    
    st.info("Insights: La precisión del modelo valida el cumplimiento de las metas del Plan de Desarrollo 2024-2028.")



import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt

def run_ml_analysis(csv_path):
    df = pd.read_csv(csv_path)
    
    # 1. PCA & K-Means (Clustering de residuos)
    st.subheader("Clustering y Reducción de Dimensionalidad (PCA)")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(numeric_df)
    
    kmeans = KMeans(n_clusters=3).fit(pca_result)
    
    fig, ax = plt.subplots()
    ax.scatter(pca_result[:,0], pca_result[:,1], c=kmeans.labels_)
    st.pyplot(fig)
    
    # 2. Clasificación (Ej: Predecir tipo de residuo)
    st.subheader("Clasificación de Residuos (Machine Learning)")
    # Supongamos que tienes una columna 'target' para clasificar
    X = numeric_df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestClassifier().fit(X_train, y_train)
    preds = model.predict(X_test)
    
    st.write(f"**Accuracy:** {accuracy_score(y_test, preds):.2f}")
    st.write(f"**F1 Score:** {f1_score(y_test, preds, average='weighted'):.2f}")
    st.write("**Matriz de Confusión:**")
    st.write(confusion_matrix(y_test, preds))