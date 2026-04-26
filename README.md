# Proyecto 4R+T: Ecosistema de Inteligencia Operativa

## 1. Visión del Proyecto
Plataforma de gestión de economía circular diseñada para la región del Sumapaz (Fusagasugá). Este proyecto integra modelos de Machine Learning (PCA/Regresión) y un Asistente Circular (Bot) para optimizar la recolección y aprovechamiento de residuos bajo el paradigma "Electric Gold".

## 2. Metodología de Ingeniería (Ciclo de Vida)
Este proyecto no solo se enfoca en el código, sino en la **calidad del proceso**. Hemos integrado dos marcos de trabajo para asegurar un despliegue robusto y escalable:

### Metodología Agile (Sprints)
* **Iteración Continua:** Desarrollo basado en ciclos cortos (Sprints) que permitieron integrar retroalimentación técnica y corregir desviaciones rápidamente.
* **Adaptabilidad:** La arquitectura evolucionó basándose en la necesidad real de despliegue en la nube, priorizando la entrega de valor funcional sobre la complejidad innecesaria.

### Gestión de Calidad (Six Sigma - D.M.A.I.C)
Para garantizar la fiabilidad del sistema, aplicamos el ciclo de mejora continua:
* **Define:** Objetivo claro: Despliegue de una solución de IA/ML en la nube (Streamlit Cloud).
* **Measure:** Monitoreo activo de errores de compilación y tiempo de respuesta.
* **Analyze:** Identificación de cuellos de botella (nomenclatura, dependencias, permisos OAuth).
* **Improve:** Refactorización a arquitectura estándar (`app.py` + `requirements.txt`).
* **Control:** Estandarización de procesos para facilitar la escalabilidad y el mantenimiento futuro.

## 3. Arquitectura Técnica
* **Lenguaje:** Python 3.12
* **Framework:** Streamlit (UI/Dashboard)
* **Inteligencia Artificial:** Scikit-learn (PCA, Regresión), Pandas, Gemini API
* **Infraestructura:** Despliegue optimizado en Streamlit Cloud
* **Automatización:** n8n / Telegram API

### Estructura del Repositorio
```text
/
├── app.py              # Punto de entrada principal (UI/Dashboard)
├── requirements.txt    # Manifiesto de dependencias del entorno
├── /src                # Lógica del modelo y servicios
├── /notebooks          # Análisis exploratorio (EDA) y entrenamiento
└── README.md           # Documentación técnica

Conclusión y Cumplimiento Normativo
Este proyecto ha sido desarrollado por William Cabezas Mejia, en su rol como Junior ML/IA Engineer (Contacto: williamcabezasmejiaudec@gmail.com),
bajo estrictos estándares de integridad y propiedad intelectual. La plataforma opera bajo el marco de seguridad de la información ISO/IEC 27001, 
garantizando la privacidad de los datos mediante encriptación bcrypt en credenciales y logs de auditoría ambiental inmutables,
asegurando una separación clara entre la trazabilidad privada de los generadores y el impacto público del dashboard.

La propiedad intelectual del código fuente, los modelos de Machine Learning, el sistema de identidad visual "Electric Gold" y los conceptos de "Guardianes del Primer Paso"
y "Sincronización Circular", son titularidad exclusiva de 4R+T SAS, con registro ante la Dirección Nacional de Derecho de Autor (DNDA) en proceso bajo licencia propietaria.
Adicionalmente, el núcleo de esta innovación, el "Sistema y método para la trazabilidad integral de residuos sólidos mediante inteligencia artificial",
cuenta con una patente en trámite ante la Superintendencia de Industria y Comercio (SIC) de Colombia (Clasificación CIP: G06Q 50/28 + G06N 20/00),
consolidando este desarrollo como una solución tecnológica protegida y de alto impacto para la gestión de residuos a escala Nacional.
